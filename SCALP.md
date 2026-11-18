# Range-Scalp Bot

*Updated Wed Nov 18 05:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63648 | 55506 | 8142 (118) | 0 | $-17436.89 | -4.4% |
| **+10¢** | 47552 | 38023 | 9529 (159) | 0 | $-16359.13 | -5.5% |
| **+15¢** | 39872 | 29597 | 10275 (204) | 0 | $-14837.03 | -5.9% |
| **+20¢** | 35514 | 24731 | 10783 (259) | 0 | $-13107.60 | -5.9% |
| **+10¢ (15¢ stop)** | 77449 | 77291 | 158 (93) | 0 | $-28459.01 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 05:20 | +5 | BNB | UP | 0.67 | 0.73 | 0.30 |
| 11-18 05:18 | +10 stop | DOGE | UP | 0.61 | 0.73 | 0.89 |
| 11-18 05:18 | +20 | DOGE | UP | 0.62 | 0.84 | 1.93 |
| 11-18 05:18 | +15 | DOGE | UP | 0.63 | 0.84 | 1.83 |
| 11-18 05:18 | +10 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-18 05:18 | +5 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-18 05:17 | +10 stop | XRP | UP | 0.69 | 0.88 | 1.67 |
| 11-18 05:17 | +10 | XRP | UP | 0.69 | 0.88 | 1.67 |
| 11-18 05:17 | +5 | XRP | UP | 0.69 | 0.74 | 0.21 |
| 11-18 05:16 | +10 stop | BNB | UP | 0.68 | 0.78 | 0.71 |
| 11-18 05:16 | +20 | BNB | UP | 0.69 | 0.90 | 1.88 |
| 11-18 05:16 | +15 | BNB | UP | 0.69 | 0.87 | 1.57 |
| 11-18 05:16 | +10 | BNB | UP | 0.68 | 0.78 | 0.71 |
| 11-18 05:16 | +5 | BNB | UP | 0.68 | 0.74 | 0.30 |
| 11-18 05:15 | +10 stop | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-18 05:15 | +20 | XRP | UP | 0.60 | 0.88 | 2.55 |
| 11-18 05:15 | +15 | XRP | UP | 0.60 | 0.88 | 2.55 |
| 11-18 05:15 | +10 | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-18 05:15 | +5 | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-18 05:13 | +10 stop | NEAR | DOWN | 0.30 | 0.66 | 3.29 |
| 11-18 05:12 | +10 stop | NEAR | DOWN | 0.65 | 0.47 | -2.14 |
| 11-18 05:12 | +20 | NEAR | DOWN | 0.65 | yes | -6.66 |
| 11-18 05:12 | +15 | NEAR | DOWN | 0.65 | yes | -6.66 |
| 11-18 05:12 | +10 | NEAR | DOWN | 0.65 | yes | -6.66 |
| 11-18 05:12 | +5 | NEAR | DOWN | 0.65 | yes | -6.66 |
| 11-18 05:12 | +10 stop | DOGE | DOWN | 0.69 | 0.54 | -1.83 |
| 11-18 05:12 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.20 |
| 11-18 05:11 | +10 stop | XRP | DOWN | 0.68 | 0.48 | -2.34 |
| 11-18 05:11 | +20 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-18 05:11 | +15 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-18 05:11 | +10 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-18 05:11 | +5 | XRP | DOWN | 0.67 | yes | -6.90 |
| 11-18 05:10 | +10 | BNB | UP | 0.62 | 0.74 | 0.89 |
| 11-18 05:10 | +5 | BNB | UP | 0.62 | 0.69 | 0.38 |
| 11-18 05:10 | +10 stop | ETH | UP | 0.51 | 0.63 | 0.85 |
| 11-18 05:10 | +10 stop | DOGE | DOWN | 0.71 | 0.43 | -3.13 |
| 11-18 05:10 | +20 | DOGE | DOWN | 0.71 | yes | -7.25 |
| 11-18 05:10 | +15 | DOGE | DOWN | 0.71 | yes | -7.25 |
| 11-18 05:10 | +10 | DOGE | DOWN | 0.71 | yes | -7.25 |
| 11-18 05:10 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
