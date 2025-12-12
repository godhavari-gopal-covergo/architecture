# Agent Migration Schema Documentation

This directory contains JSON schemas for extracting and migrating agent data from legacy systems to CoverGo's platform.

## Schema Files

### 1. `agent-migration-schema.json`

The complete, nested JSON schema that follows the structure expected by CoverGo's GraphQL API. This schema includes:

- **Agent entity** with all properties from the dynamic schema
- **Embedded Distributor** schema with full structure
- **Distributor Team** schema for team hierarchy
- **Sales Channel** schema for channel information
- **Audit** information for tracking changes

**Use this schema when:**
- You need full validation of migration data
- Your data extraction tool can handle nested structures
- You want to migrate data that matches the API structure exactly

### 2. `agent-migration-flat-schema.json`

A flattened version of the schema suitable for CSV/Excel imports. All nested properties are prefixed with their parent object name (e.g., `distributor_distributorName`).

**Use this schema when:**
- Importing from spreadsheets or CSV files
- Your legacy system exports flat data structures
- You need a simpler mapping process

### 3. `sample-agent-migration-data.json`

Sample data demonstrating both regular agents and virtual agents with all fields populated.

## Reference Data Types

The following reference data types are used in the schemas:

| Reference Type | Description | Example Values |
|----------------|-------------|----------------|
| `TTL` | Salutation/Title | Mr, Mrs, Ms, Dr |
| `CRY` | Country Code | HK, US, GB, SG |
| `CCY` | Currency Code | HKD, USD, EUR, GBP |
| `BNK` | Bank Identifier | HSBC, SCB, BOC |
| `BRH` | Bank Branch | 001, 002, etc. |
| `X-PRD-AGTSUSPENSIONREASON` | Suspension Reason | Custom values |
| `X-PRD-BILLFREQ` | Billing Frequency | monthly, quarterly, annually |

## Field Requirements

### Required Fields for Agent Migration

| Field | Description |
|-------|-------------|
| `agentNumber` | Unique agent identifier/code |
| `firstName` | Agent's first name |
| `surname` | Agent's surname |
| `salutation` | Title (TTL reference) |
| `distributorId` | Parent distributor ID |
| `distributorTeamId` | Team ID within distributor |
| `activeFromDateTime` | Date agent becomes active |

### Conditional Requirements

- **Contact information** (`addrLine1`, `postCode`, `countryCode`, `mainContactEmail`, `mainContactPhone`) is required when `isVirtualAgent` is `false`
- **Virtual agent name** is required when `isVirtualAgent` is `true`

## Entity Relationships

```
Sales Channel
    └── Distributor
            ├── Party (contact info)
            ├── Bank Information
            ├── Commissions Configuration
            ├── Payment Data
            └── Teams
                    └── Agents
                            ├── Basic Info
                            ├── Distribution Info
                            ├── Contact Info
                            ├── Bank Information
                            ├── Access Control
                            └── Payment Settings
```

## Migration Steps

1. **Extract Distributors First**
   - Export all distributors with their teams
   - Validate against the distributor portion of the schema
   - Import distributors and teams to get IDs

2. **Extract Agents**
   - Export agents with references to distributor and team IDs
   - Validate against the full agent schema
   - Import agents linked to their distributors

3. **Verify Relationships**
   - Confirm all agents are linked to valid distributors
   - Confirm all agents are assigned to valid teams
   - Verify reference data codes match the target system

## GraphQL API Reference

The schemas are based on the CoverGo GraphQL API types:

- `agent` - Main agent entity
- `requestManager_IAgents_Agents_Items_Party` - Agent party/contact info
- `requestManager_IDistributors_Distributors_Items` - Distributor entity
- `requestManager_IDistributors_Distributors_Items_Party` - Distributor party info
- `requestManager_IDistributors_Distributors_Items_PaymentData` - Payment config
- `distributorTeam` - Team entity with hierarchy support
- `requestManager_ISalesChannels_SalesChannels_Items` - Sales channel entity

## Validation

Both schemas follow JSON Schema Draft-07 specification and can be validated using:

```bash
# Using ajv-cli
npx ajv validate -s agent-migration-schema.json -d your-data.json

# Using Python jsonschema
python -m jsonschema -i your-data.json agent-migration-schema.json
```

## Example: Flat Data for CSV Import

```csv
agentNumber,firstName,surname,salutation,distributorId,distributorTeamId,activeFromDateTime,isVirtualAgent,mainContactEmail,mainContactPhone,countryCode
AGT001,John,Smith,Mr,DIST001,TEAM001,2024-01-01,false,john@example.com,+85212345678,HK
AGT002,Virtual,Agent,N/A,DIST001,TEAM001,2024-01-01,true,,,
```

## Support

For questions about the migration schema or API, refer to the CoverGo GraphQL API documentation at:
- API Endpoint: `https://api.uat.ca.covergo.cloud/graphql`
- Use GraphQL introspection for the latest type definitions
