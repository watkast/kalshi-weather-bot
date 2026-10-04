# Range-Scalp Bot

*Updated Sun Oct 04 13:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 2278 | 1963 | 315 (3) | 0 | $-773.65 | -5.4% |
| **+10¢** | 1775 | 1426 | 349 (4) | 0 | $-577.75 | -5.2% |
| **+15¢** | 1494 | 1124 | 370 (5) | 0 | $-487.07 | -5.2% |
| **+20¢** | 1322 | 933 | 389 (8) | 0 | $-426.87 | -5.1% |
| **+10¢ (15¢ stop)** | 2819 | 2818 | 1 (1) | 0 | $-1056.41 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 12:55 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-04 12:54 | +10 stop | NEAR | UP | 0.46 | 0.57 | 0.74 |
| 10-04 12:51 | +10 stop | DOGE | DOWN | 0.71 | 0.86 | 1.26 |
| 10-04 12:51 | +10 stop | ZEC | UP | 0.53 | 0.25 | -3.12 |
| 10-04 12:51 | +20 | ZEC | UP | 0.53 | no | -5.48 |
| 10-04 12:51 | +15 | ZEC | UP | 0.53 | no | -5.48 |
| 10-04 12:51 | +10 | ZEC | UP | 0.53 | no | -5.48 |
| 10-04 12:51 | +5 | ZEC | UP | 0.53 | no | -5.48 |
| 10-04 12:50 | +10 stop | NEAR | UP | 0.57 | 0.67 | 0.66 |
| 10-04 12:49 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 10-04 12:48 | +5 | DOGE | DOWN | 0.70 | 0.78 | 0.52 |
| 10-04 12:47 | +5 | BNB | DOWN | 0.67 | yes | -6.88 |
| 10-04 12:46 | +10 stop | DOGE | DOWN | 0.67 | 0.45 | -2.54 |
| 10-04 12:46 | +20 | DOGE | DOWN | 0.67 | 0.92 | 2.24 |
| 10-04 12:46 | +15 | DOGE | DOWN | 0.67 | 0.86 | 1.65 |
| 10-04 12:46 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-04 12:46 | +5 | DOGE | DOWN | 0.67 | 0.73 | 0.30 |
| 10-04 12:46 | +10 stop | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 10-04 12:46 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 10-04 12:46 | +15 | ETH | DOWN | 0.64 | 0.79 | 1.21 |
| 10-04 12:46 | +10 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 10-04 12:46 | +5 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 10-04 12:46 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-04 12:46 | +20 | XRP | DOWN | 0.63 | 0.86 | 2.04 |
| 10-04 12:46 | +15 | XRP | DOWN | 0.63 | 0.86 | 2.04 |
| 10-04 12:46 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-04 12:46 | +5 | XRP | DOWN | 0.63 | 0.72 | 0.58 |
| 10-04 12:46 | +10 stop | NEAR | UP | 0.70 | 0.55 | -1.83 |
| 10-04 12:46 | +20 | NEAR | UP | 0.70 | no | -7.15 |
| 10-04 12:46 | +15 | NEAR | UP | 0.70 | no | -7.15 |
| 10-04 12:46 | +10 | NEAR | UP | 0.70 | no | -7.15 |
| 10-04 12:46 | +5 | NEAR | UP | 0.70 | no | -7.15 |
| 10-04 12:46 | +10 stop | BNB | DOWN | 0.65 | 0.43 | -2.53 |
| 10-04 12:46 | +20 | BNB | DOWN | 0.65 | yes | -6.65 |
| 10-04 12:46 | +15 | BNB | DOWN | 0.65 | yes | -6.65 |
| 10-04 12:46 | +10 | BNB | DOWN | 0.65 | yes | -6.65 |
| 10-04 12:46 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.20 |
| 10-04 12:45 | +10 stop | HYPE | DOWN | 0.66 | 0.84 | 1.54 |
| 10-04 12:45 | +20 | HYPE | DOWN | 0.66 | 0.89 | 2.07 |
| 10-04 12:45 | +15 | HYPE | DOWN | 0.66 | 0.84 | 1.54 |
