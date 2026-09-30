// The email a developer sends their engineering manager from the "Bring this
// to your team" section. Source: workshops repo,
// 2-marketing/channels/outreach/pitch-your-manager/en-email.md and de-email.md.
// A mailto cannot attach a file, so the line about the attached one-pager
// links to the copy this site serves instead. Keep both in step with the kit.

const onePagerUrl = "https://unvibe.org/public/agentic-engineering-workshop.pdf";
const utm = "utm_source=pitch-kit&utm_medium=email&utm_campaign=pitch-your-manager";
const siteUrl = `https://unvibe.org/?${utm}`;
const callUrl = `https://cal.com/dominik1001/workshop?${utm}`;

const en = {
    subject: "A workshop day for our team: agentic engineering, on site",
    paragraphs: [
        "Hi [Name],",
        "I came across a one-day workshop I'd like us to do as a team: the Agentic Engineering Workshop by unvibe. It's a full day at our office where we work with Claude Code on a project they bring, from the first plan to reviewed, working code, with instructors who ship production code with agents every day.",
        "Why I'm asking: [one line on what you want from it, for example: we all use AI tools, and I think we'd get more out of them with shared rules for the agent and a review workflow that keeps up with the pull requests.]",
        `The facts: one day, on site, up to 20 engineers, from EUR 4,000 for a group of ten. They bring the project, so none of our code goes into an agent. The one-pager is at ${onePagerUrl} and the details are at ${siteUrl}`,
        `Would you book a 20-minute call with them to scope it? The link is ${callUrl} and I'm happy to join.`,
        "[Your name]",
    ],
};

const de = {
    subject: "Ein Workshop-Tag für unser Team: Agentic Engineering, bei uns im Haus",
    paragraphs: [
        "Hallo [Name],",
        "ich bin auf einen eintägigen Workshop gestoßen, den ich gern mit dem Team machen würde: den Agentic Engineering Workshop von unvibe. Ein ganzer Tag bei uns im Büro, in dem wir mit Claude Code an einem Projekt arbeiten, das die Instructors mitbringen, vom ersten Plan bis zu reviewtem, laufendem Code. Die Instructors schreiben selbst täglich Production-Code mit Agents.",
        "Warum ich frage: [ein Satz dazu, was du dir davon versprichst, zum Beispiel: wir nutzen alle AI-Tools, und ich glaube, mit gemeinsamen Regeln für den Agent und einem Review-Workflow, der mit den Pull Requests mithält, holen wir deutlich mehr raus.]",
        `Die Eckdaten: ein Tag, bei uns vor Ort, bis zu 20 Entwickler, ab 4.000 EUR für eine Gruppe von zehn. Das Projekt bringen sie mit, unser Code geht also nicht in einen Agent. Den One-Pager gibt es unter ${onePagerUrl} und Details stehen auf ${siteUrl}`,
        `Würdest du ein 20-minütiges Gespräch mit ihnen buchen, um den Tag abzustecken? Der Link ist ${callUrl} und ich bin gern dabei.`,
        "[Dein Name]",
    ],
};

// No recipient: the developer fills in their manager. RFC 6068 wants CRLF
// line breaks in the body.
function mailto({ subject, paragraphs }: { subject: string; paragraphs: string[] }) {
    const body = paragraphs.join("\r\n\r\n");
    return `mailto:?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}

export const managerEmailEn = mailto(en);
export const managerEmailDe = mailto(de);
export const onePagerPath = "/public/agentic-engineering-workshop.pdf";
