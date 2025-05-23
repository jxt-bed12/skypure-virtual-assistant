-- Customers table
create table customers (
  id bigint primary key generated by default as identity,
  name text not null,
  phone_number text not null,
  location text not null,
  language_preference text not null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Interactions table
create table interactions (
  id bigint primary key generated by default as identity,
  customer_id bigint references customers(id),
  query_type text not null,
  resolved boolean default false,
  notes text,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Feedback table
create table feedback (
  id bigint primary key generated by default as identity,
  customer_id bigint references customers(id),
  rating integer check (rating >= 1 and rating <= 5),
  comments text,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);