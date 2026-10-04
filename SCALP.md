# Range-Scalp Bot

*Updated Sun Oct 04 04:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 1747 | 1504 | 243 (3) | 3 | $-595.73 | -5.4% |
| **+10¢** | 1355 | 1087 | 268 (4) | 5 | $-427.59 | -5.0% |
| **+15¢** | 1143 | 861 | 282 (5) | 5 | $-348.27 | -4.8% |
| **+20¢** | 1005 | 704 | 301 (7) | 6 | $-359.20 | -5.7% |
| **+10¢ (15¢ stop)** | 2207 | 2206 | 1 (1) | 4 | $-931.85 | -6.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-04 04:19 | +5 | BNB | DOWN | 0.65 | open |  |
| 10-04 04:19 | +10 stop | ETH | DOWN | 0.69 | open |  |
| 10-04 04:19 | +10 | ETH | DOWN | 0.69 | open |  |
| 10-04 04:19 | +5 | ETH | DOWN | 0.69 | open |  |
| 10-04 04:19 | +5 | BNB | DOWN | 0.56 | 0.61 | 0.15 |
| 10-04 04:18 | +10 stop | SOL | DOWN | 0.48 | open |  |
| 10-04 04:18 | +10 stop | BNB | DOWN | 0.61 | 0.38 | -2.64 |
| 10-04 04:18 | +20 | BNB | DOWN | 0.61 | open |  |
| 10-04 04:18 | +15 | BNB | DOWN | 0.61 | open |  |
| 10-04 04:18 | +10 | BNB | DOWN | 0.61 | open |  |
| 10-04 04:18 | +5 | BNB | DOWN | 0.61 | 0.68 | 0.37 |
| 10-04 04:17 | +10 stop | ZEC | UP | 0.66 | 0.81 | 1.23 |
| 10-04 04:17 | +20 | ZEC | UP | 0.66 | 0.86 | 1.75 |
| 10-04 04:17 | +15 | ZEC | UP | 0.66 | 0.81 | 1.23 |
| 10-04 04:17 | +10 | ZEC | UP | 0.66 | 0.81 | 1.23 |
| 10-04 04:17 | +5 | ZEC | UP | 0.66 | 0.73 | 0.40 |
| 10-04 04:17 | +10 stop | HYPE | DOWN | 0.69 | open |  |
| 10-04 04:17 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-04 04:17 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-04 04:17 | +10 | HYPE | DOWN | 0.69 | open |  |
| 10-04 04:17 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.25 |
| 10-04 04:16 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-04 04:16 | +20 | ETH | DOWN | 0.62 | open |  |
| 10-04 04:16 | +15 | ETH | DOWN | 0.62 | open |  |
| 10-04 04:16 | +10 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-04 04:16 | +5 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-04 04:16 | +10 stop | SOL | UP | 0.63 | 0.47 | -1.95 |
| 10-04 04:16 | +20 | SOL | UP | 0.63 | open |  |
| 10-04 04:16 | +15 | SOL | UP | 0.63 | open |  |
| 10-04 04:16 | +10 | SOL | UP | 0.64 | open |  |
| 10-04 04:16 | +5 | SOL | UP | 0.64 | open |  |
| 10-04 04:16 | +10 stop | DOGE | UP | 0.57 | 0.74 | 1.38 |
| 10-04 04:16 | +20 | DOGE | UP | 0.57 | 0.77 | 1.69 |
| 10-04 04:16 | +15 | DOGE | UP | 0.57 | 0.74 | 1.38 |
| 10-04 04:16 | +10 | DOGE | UP | 0.57 | 0.74 | 1.38 |
| 10-04 04:16 | +5 | DOGE | UP | 0.57 | 0.74 | 1.38 |
| 10-04 04:16 | +10 stop | HYPE | DOWN | 0.56 | 0.76 | 1.69 |
| 10-04 04:16 | +20 | HYPE | DOWN | 0.56 | 0.76 | 1.69 |
| 10-04 04:16 | +15 | HYPE | DOWN | 0.56 | 0.76 | 1.69 |
| 10-04 04:16 | +10 | HYPE | DOWN | 0.56 | 0.76 | 1.69 |
