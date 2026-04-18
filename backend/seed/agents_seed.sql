-- agents_seed.sql
-- Seed initial agents for the platform
INSERT INTO agents (name, description, version) VALUES
    ('Tomas', 'Core orchestrator agent', '1.0'),
    ('CTO', 'Technical leadership agent', '1.0'),
    ('CPO', 'Product ownership agent', '1.0'),
    ('CMO', 'Marketing strategy agent', '1.0'),
    ('CFO', 'Financial management agent', '1.0');
