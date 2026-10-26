# Range-Scalp Bot

*Updated Mon Oct 26 01:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34079 | 29754 | 4325 (43) | 0 | $-9418.51 | -4.4% |
| **+10¢** | 25509 | 20506 | 5003 (65) | 0 | $-8272.07 | -5.2% |
| **+15¢** | 21331 | 15946 | 5385 (89) | 0 | $-7388.65 | -5.5% |
| **+20¢** | 18902 | 13262 | 5640 (111) | 0 | $-6483.24 | -5.5% |
| **+10¢ (15¢ stop)** | 41741 | 41679 | 62 (33) | 0 | $-15883.43 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 01:36 | +10 stop | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-26 01:35 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-26 01:35 | +10 stop | ZEC | UP | 0.54 | 0.34 | -2.34 |
| 10-26 01:35 | +5 | ZEC | UP | 0.55 | 0.63 | 0.45 |
| 10-26 01:34 | +5 | BNB | DOWN | 0.67 | 0.74 | 0.40 |
| 10-26 01:34 | +5 | ZEC | DOWN | 0.56 | 0.65 | 0.56 |
| 10-26 01:34 | +10 stop | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-26 01:34 | +10 | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-26 01:34 | +5 | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 10-26 01:34 | +5 | XRP | DOWN | 0.61 | 0.77 | 1.30 |
| 10-26 01:34 | +10 stop | BTC | DOWN | 0.49 | 0.62 | 0.95 |
| 10-26 01:34 | +10 stop | SOL | DOWN | 0.55 | 0.67 | 0.86 |
| 10-26 01:33 | +10 stop | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 10-26 01:33 | +20 | DOGE | DOWN | 0.66 | 0.86 | 1.76 |
| 10-26 01:33 | +15 | DOGE | DOWN | 0.66 | 0.86 | 1.76 |
| 10-26 01:33 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.72 |
| 10-26 01:33 | +5 | DOGE | DOWN | 0.66 | 0.76 | 0.72 |
| 10-26 01:33 | +10 stop | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-26 01:33 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 10-26 01:33 | +15 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-26 01:33 | +10 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 10-26 01:33 | +5 | ETH | DOWN | 0.67 | 0.75 | 0.50 |
| 10-26 01:33 | +10 stop | BNB | DOWN | 0.70 | 0.84 | 1.11 |
| 10-26 01:33 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 10-26 01:33 | +5 | BNB | DOWN | 0.67 | 0.74 | 0.40 |
| 10-26 01:33 | +10 stop | ZEC | DOWN | 0.64 | 0.40 | -2.74 |
| 10-26 01:33 | +20 | ZEC | DOWN | 0.64 | 0.84 | 1.73 |
| 10-26 01:33 | +15 | ZEC | DOWN | 0.64 | 0.84 | 1.73 |
| 10-26 01:33 | +10 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-26 01:33 | +5 | ZEC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-26 01:33 | +10 stop | XRP | DOWN | 0.62 | 0.77 | 1.22 |
| 10-26 01:33 | +20 | XRP | DOWN | 0.62 | 0.83 | 1.85 |
| 10-26 01:33 | +15 | XRP | DOWN | 0.62 | 0.77 | 1.22 |
| 10-26 01:33 | +10 | XRP | DOWN | 0.62 | 0.77 | 1.22 |
| 10-26 01:33 | +5 | XRP | DOWN | 0.61 | 0.66 | 0.17 |
| 10-26 01:31 | +10 stop | BTC | DOWN | 0.65 | 0.47 | -2.14 |
| 10-26 01:31 | +20 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 10-26 01:31 | +15 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 10-26 01:31 | +10 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 10-26 01:31 | +5 | BTC | DOWN | 0.66 | 0.74 | 0.50 |
