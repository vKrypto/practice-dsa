```
SQL Index Types
├── By Structure
│   ├── Clustered Index
│   └── Non-Clustered Index
│
├── By Column Coverage
│   ├── Single-Column Index
│   ├── Multi-Column (Composite) Index
│   └── Covering Index (with included columns)  # store seperate copy of those columns for faster query
│
├── By Uniqueness
│   └── Unique Index
│
├── By Filter Condition
│   └── Filtered / Partial Index
│
├── By Data Type
│   ├── Full-Text Index
│   └── Spatial Index
│
└── Engine-Specific / Optimization
    └── Bitmap Index


MongoDB Indexes
├── Basic Indexes
│   ├── Single Field Index
│   │   └─ Speeds up queries filtering/sorting on one field.
│   └── Compound Index
│       └─ Optimizes queries using multiple fields in sequence.
│
├── Special Indexes
│   ├── Multikey Index
│   │   └─ Enables indexing fields that hold arrays.
│   ├── Text Index
│   │   └─ Enables full-text search in string content.
│   ├── Hashed Index
│   │   └─ Shards data evenly using a hashed field value.
│   └── Wildcard Index
│       └─ Indexes multiple fields without explicitly naming them.
│
├── Geospatial Indexes
│   ├── 2d Index
│   │   └─ Supports flat Earth (planar) coordinate queries.
│   └── 2dsphere Index
│       └─ Supports spherical (Earth-like) geo queries.
│
└── TTL & Partial Indexes
    ├── TTL (Time-To-Live) Index
    │   └─ Automatically deletes documents after a time limit.
    └── Partial Index
        └─ Indexes only documents that match a filter expression.


PostgreSQL Indexes
├── I. Standard Indexes
│   ├── B-tree Index
│   │   └─ Default index; supports equality and range queries.
│   └── Hash Index
│       └─ Optimized for equality checks (e.g., WHERE col = val).
│
├── II. Advanced Indexes
│   ├── GIN (Generalized Inverted Index)
│   │   └─ Ideal for array, JSONB, full-text search (multiple values per row).
│   ├── GiST (Generalized Search Tree)
│   │   └─ Supports geometric, range, and fuzzy search queries.
│   ├── SP-GiST (Space-Partitioned GiST)
│   │   └─ Efficient for partitioned data like prefix trees or hierarchies.
│   └── BRIN (Block Range Index)
│       └─ Lightweight index for large, naturally ordered, append-only tables.
│
├── III. Functional Indexes
│   └── Expression Index
│       └─ Indexes results of expressions/functions (e.g., LOWER(name)).
│
├── IV. Conditional Indexes
│   └── Partial Index
│       └─ Indexes only rows matching a WHERE condition (e.g., active=true).
│
├── V. Unique Constraints as Indexes
│   └── Unique Index
│       └─ Enforces uniqueness of column(s) and improves read performance.
│
├── VI. Composite Indexes
│   └── Multi-Column Index
│       └─ Indexes multiple columns; respects left-to-right order in lookups.
│
└── VII. Concurrent Indexes
    └── Concurrent Index
        └─ Allows index creation without locking writes on the table.
```