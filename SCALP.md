# Range-Scalp Bot

*Updated Mon Nov 09 07:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53490 | 46639 | 6851 (85) | 1 | $-14768.14 | -4.4% |
| **+10¢** | 39961 | 31971 | 7990 (110) | 1 | $-13762.39 | -5.5% |
| **+15¢** | 33485 | 24876 | 8609 (141) | 1 | $-12556.26 | -6.0% |
| **+20¢** | 29795 | 20766 | 9029 (186) | 2 | $-11061.02 | -5.9% |
| **+10¢ (15¢ stop)** | 65175 | 65069 | 106 (63) | 0 | $-24094.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 07:36 | +10 stop | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 11-09 07:36 | +10 | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 11-09 07:36 | +5 | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 11-09 07:35 | +10 stop | NEAR | UP | 0.62 | 0.73 | 0.81 |
| 11-09 07:35 | +10 stop | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 11-09 07:34 | +10 stop | ETH | UP | 0.69 | 0.79 | 0.73 |
| 11-09 07:34 | +20 | ETH | UP | 0.69 | 0.91 | 1.99 |
| 11-09 07:34 | +10 | ETH | UP | 0.69 | 0.79 | 0.73 |
| 11-09 07:34 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 11-09 07:34 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 11-09 07:34 | +10 | SOL | UP | 0.67 | 0.80 | 1.02 |
| 11-09 07:34 | +5 | SOL | UP | 0.68 | 0.73 | 0.20 |
| 11-09 07:34 | +10 stop | NEAR | DOWN | 0.70 | 0.55 | -1.83 |
| 11-09 07:34 | +20 | NEAR | DOWN | 0.70 | open |  |
| 11-09 07:34 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-09 07:34 | +10 | NEAR | DOWN | 0.71 | open |  |
| 11-09 07:34 | +5 | NEAR | DOWN | 0.71 | open |  |
| 11-09 07:33 | +5 | XRP | UP | 0.68 | 0.75 | 0.40 |
| 11-09 07:33 | +10 stop | BNB | UP | 0.67 | 0.77 | 0.71 |
| 11-09 07:33 | +10 | BNB | UP | 0.67 | 0.77 | 0.71 |
| 11-09 07:33 | +5 | BNB | UP | 0.67 | 0.74 | 0.40 |
| 11-09 07:33 | +5 | DOGE | UP | 0.68 | 0.81 | 1.03 |
| 11-09 07:32 | +10 stop | HYPE | UP | 0.67 | 0.52 | -1.84 |
| 11-09 07:32 | +20 | HYPE | UP | 0.67 | open |  |
| 11-09 07:32 | +15 | HYPE | UP | 0.67 | 0.84 | 1.44 |
| 11-09 07:32 | +10 | HYPE | UP | 0.67 | 0.84 | 1.44 |
| 11-09 07:32 | +5 | HYPE | UP | 0.67 | 0.72 | 0.19 |
| 11-09 07:31 | +10 stop | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 11-09 07:31 | +20 | DOGE | UP | 0.61 | 0.81 | 1.72 |
| 11-09 07:31 | +15 | DOGE | UP | 0.61 | 0.81 | 1.72 |
| 11-09 07:31 | +10 | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 11-09 07:31 | +5 | DOGE | UP | 0.61 | 0.69 | 0.48 |
| 11-09 07:31 | +10 stop | ZEC | UP | 0.62 | 0.72 | 0.68 |
| 11-09 07:31 | +20 | ZEC | UP | 0.61 | 0.81 | 1.72 |
| 11-09 07:31 | +15 | ZEC | UP | 0.61 | 0.81 | 1.69 |
| 11-09 07:31 | +10 | ZEC | UP | 0.61 | 0.72 | 0.75 |
| 11-09 07:31 | +5 | ZEC | UP | 0.61 | 0.72 | 0.75 |
| 11-09 07:31 | +10 stop | XRP | UP | 0.68 | 0.82 | 1.13 |
| 11-09 07:31 | +20 | XRP | UP | 0.68 | 0.91 | 2.05 |
| 11-09 07:31 | +15 | XRP | UP | 0.67 | 0.82 | 1.23 |
