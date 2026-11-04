# Range-Scalp Bot

*Updated Wed Nov 04 04:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46805 | 40760 | 6045 (72) | 0 | $-13446.70 | -4.6% |
| **+10¢** | 34963 | 27955 | 7008 (96) | 0 | $-12268.20 | -5.6% |
| **+15¢** | 29278 | 21737 | 7541 (124) | 0 | $-11218.68 | -6.1% |
| **+20¢** | 26010 | 18112 | 7898 (164) | 0 | $-9871.88 | -6.1% |
| **+10¢ (15¢ stop)** | 57059 | 56966 | 93 (56) | 0 | $-21320.64 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 04:19 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.25 |
| 11-04 04:19 | +10 stop | BTC | DOWN | 0.55 | 0.65 | 0.66 |
| 11-04 04:18 | +5 | ETH | DOWN | 0.63 | 0.71 | 0.48 |
| 11-04 04:18 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 11-04 04:18 | +10 | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 11-04 04:18 | +5 | SOL | DOWN | 0.65 | 0.71 | 0.29 |
| 11-04 04:17 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-04 04:16 | +10 stop | BNB | DOWN | 0.61 | 0.72 | 0.74 |
| 11-04 04:16 | +20 | BNB | DOWN | 0.61 | 0.82 | 1.78 |
| 11-04 04:16 | +15 | BNB | DOWN | 0.61 | 0.81 | 1.68 |
| 11-04 04:16 | +10 | BNB | DOWN | 0.61 | 0.72 | 0.74 |
| 11-04 04:16 | +5 | BNB | DOWN | 0.61 | 0.67 | 0.23 |
| 11-04 04:16 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 11-04 04:16 | +20 | ETH | DOWN | 0.62 | 0.82 | 1.72 |
| 11-04 04:16 | +15 | ETH | DOWN | 0.62 | 0.77 | 1.20 |
| 11-04 04:16 | +10 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 11-04 04:16 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-04 04:16 | +10 stop | BTC | DOWN | 0.65 | 0.50 | -1.84 |
| 11-04 04:16 | +20 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-04 04:16 | +15 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-04 04:16 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-04 04:16 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
| 11-04 04:16 | +10 stop | ZEC | DOWN | 0.59 | 0.72 | 0.98 |
| 11-04 04:16 | +20 | ZEC | DOWN | 0.58 | 0.82 | 2.11 |
| 11-04 04:16 | +15 | ZEC | DOWN | 0.58 | 0.75 | 1.38 |
| 11-04 04:16 | +10 | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-04 04:16 | +5 | ZEC | DOWN | 0.58 | 0.63 | 0.15 |
| 11-04 04:16 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-04 04:16 | +20 | XRP | DOWN | 0.66 | 0.87 | 1.86 |
| 11-04 04:16 | +15 | XRP | DOWN | 0.66 | 0.81 | 1.23 |
| 11-04 04:16 | +10 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-04 04:16 | +5 | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-04 04:16 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 11-04 04:16 | +20 | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-04 04:16 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-04 04:16 | +10 | HYPE | DOWN | 0.61 | 0.74 | 0.95 |
| 11-04 04:16 | +5 | HYPE | DOWN | 0.61 | 0.74 | 0.95 |
| 11-04 04:16 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-04 04:16 | +20 | SOL | DOWN | 0.61 | 0.82 | 1.82 |
| 11-04 04:16 | +15 | SOL | DOWN | 0.61 | 0.79 | 1.51 |
