export interface PricingTier {
  name: string;
  description: string;
  price: number;
  featured?: boolean;
  badge?: string;
}

export interface Sponsor {
  name: string;
  url: string;
  logo: string;
}

export interface WorkshopEvent {
  slug: string;
  date: string;
  dateDisplay: string;
  dayOfWeek: string;
  time: string;
  venue: string;
  city: string;
  lumaUrl: string;
  pricing?: PricingTier[];
  sponsors: Sponsor[];
  status?: "sold-out";
  attendeeCount?: number;
  recap?: string;
}

const sponsors: Sponsor[] = [
  { name: "Fluensy", url: "https://fluensy.app/", logo: "/public/fluensy-logotext.svg" },
  { name: "Lithus", url: "https://lithus.eu/", logo: "/public/lithus-logo.svg" },
  { name: "Marbles", url: "https://usemarbles.com/", logo: "/public/marbles-logo.svg" },
];

const upcomingPricing: PricingTier[] = [
  { name: "Early Bird", description: "Individual developers — limited seats", price: 195, featured: true },
  { name: "Regular", description: "Standard ticket", price: 350 },
  { name: "Team (3+)", description: "Per person, for groups of 3 or more", price: 295 },
];

export const events: WorkshopEvent[] = [
  {
    slug: "2026-07-17-munich",
    date: "2026-07-17",
    dateDisplay: "July 17, 2026",
    dayOfWeek: "Friday",
    time: "12:00 PM – 6:00 PM CEST",
    venue: "WERK1, Munich",
    city: "Munich",
    lumaUrl: "https://luma.com/fc92s7r4",
    pricing: upcomingPricing,
    sponsors,
  },
  {
    slug: "2026-05-13-munich",
    date: "2026-05-13",
    dateDisplay: "May 13, 2026",
    dayOfWeek: "Wednesday",
    time: "1:00 PM – 6:00 PM CEST",
    venue: "WERK1, Munich",
    city: "Munich",
    lumaUrl: "https://luma.com/lj9niymo",
    sponsors,
    attendeeCount: 15,
  },
];
