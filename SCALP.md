# Range-Scalp Bot

*Updated Wed Oct 28 01:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37350 | 32607 | 4743 (45) | 0 | $-10393.02 | -4.4% |
| **+10¢** | 27886 | 22391 | 5495 (67) | 0 | $-9285.47 | -5.3% |
| **+15¢** | 23334 | 17432 | 5902 (91) | 0 | $-8249.87 | -5.6% |
| **+20¢** | 20681 | 14505 | 6176 (116) | 0 | $-7210.87 | -5.6% |
| **+10¢ (15¢ stop)** | 45752 | 45687 | 65 (34) | 0 | $-17455.17 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 01:11 | +10 stop | ZEC | DOWN | 0.65 | 0.86 | 1.85 |
| 10-28 01:09 | +5 | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 10-28 01:09 | +10 stop | ZEC | DOWN | 0.64 | 0.48 | -1.95 |
| 10-28 01:09 | +10 stop | BTC | DOWN | 0.60 | 0.82 | 1.92 |
| 10-28 01:09 | +10 | BTC | DOWN | 0.60 | 0.82 | 1.92 |
| 10-28 01:09 | +5 | BTC | DOWN | 0.60 | 0.65 | 0.17 |
| 10-28 01:07 | +10 stop | ZEC | UP | 0.65 | 0.47 | -2.14 |
| 10-28 01:06 | +5 | BTC | DOWN | 0.70 | 0.77 | 0.42 |
| 10-28 01:06 | +10 stop | ZEC | UP | 0.47 | 0.63 | 1.25 |
| 10-28 01:05 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-28 01:05 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-28 01:05 | +20 | HYPE | DOWN | 0.61 | 0.84 | 2.03 |
| 10-28 01:05 | +15 | HYPE | DOWN | 0.61 | 0.78 | 1.40 |
| 10-28 01:05 | +10 | HYPE | DOWN | 0.59 | 0.72 | 0.98 |
| 10-28 01:05 | +5 | HYPE | DOWN | 0.59 | 0.67 | 0.47 |
| 10-28 01:04 | +5 | BTC | DOWN | 0.56 | 0.63 | 0.35 |
| 10-28 01:04 | +5 | ZEC | DOWN | 0.69 | 0.86 | 1.46 |
| 10-28 01:04 | +10 stop | ZEC | DOWN | 0.60 | 0.35 | -2.83 |
| 10-28 01:04 | +20 | ZEC | DOWN | 0.60 | 0.86 | 2.34 |
| 10-28 01:04 | +15 | ZEC | DOWN | 0.60 | 0.86 | 2.34 |
| 10-28 01:04 | +10 | ZEC | DOWN | 0.60 | 0.86 | 2.34 |
| 10-28 01:04 | +5 | ZEC | DOWN | 0.60 | 0.65 | 0.17 |
| 10-28 01:01 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-28 01:01 | +20 | BTC | DOWN | 0.66 | 0.93 | 2.51 |
| 10-28 01:01 | +15 | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 10-28 01:01 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-28 01:01 | +5 | BTC | DOWN | 0.66 | 0.73 | 0.40 |
| 10-28 01:01 | +10 stop | ZEC | DOWN | 0.66 | 0.76 | 0.71 |
| 10-28 01:01 | +20 | ZEC | DOWN | 0.66 | 0.89 | 2.07 |
| 10-28 01:01 | +15 | ZEC | DOWN | 0.71 | 0.89 | 1.58 |
| 10-28 01:01 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-28 01:01 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-28 01:01 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-28 01:01 | +20 | BNB | DOWN | 0.65 | 0.85 | 1.75 |
| 10-28 01:01 | +15 | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 10-28 01:01 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-28 01:01 | +5 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-28 01:01 | +10 stop | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 10-28 01:01 | +20 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 10-28 01:01 | +15 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
