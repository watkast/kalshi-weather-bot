# Range-Scalp Bot

*Updated Sun Nov 15 11:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60672 | 52927 | 7745 (112) | 1 | $-16449.48 | -4.3% |
| **+10¢** | 45326 | 36246 | 9080 (150) | 1 | $-15534.42 | -5.5% |
| **+15¢** | 37966 | 28170 | 9796 (188) | 3 | $-14222.34 | -6.0% |
| **+20¢** | 33840 | 23564 | 10276 (240) | 5 | $-12522.58 | -5.9% |
| **+10¢ (15¢ stop)** | 73847 | 73696 | 151 (89) | 1 | $-27173.73 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 11:16 | +10 stop | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 11-15 11:16 | +20 | DOGE | UP | 0.61 | open |  |
| 11-15 11:16 | +15 | DOGE | UP | 0.61 | 0.76 | 1.20 |
| 11-15 11:16 | +10 | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 11-15 11:16 | +5 | DOGE | UP | 0.61 | 0.70 | 0.58 |
| 11-15 11:16 | +10 stop | XRP | UP | 0.62 | 0.74 | 0.89 |
| 11-15 11:16 | +20 | XRP | UP | 0.62 | open |  |
| 11-15 11:16 | +15 | XRP | UP | 0.62 | open |  |
| 11-15 11:16 | +10 | XRP | UP | 0.62 | 0.74 | 0.89 |
| 11-15 11:16 | +5 | XRP | UP | 0.62 | 0.70 | 0.48 |
| 11-15 11:16 | +10 stop | HYPE | UP | 0.68 | open |  |
| 11-15 11:16 | +20 | HYPE | UP | 0.67 | open |  |
| 11-15 11:16 | +15 | HYPE | UP | 0.66 | open |  |
| 11-15 11:16 | +10 | HYPE | UP | 0.66 | open |  |
| 11-15 11:16 | +5 | HYPE | UP | 0.66 | open |  |
| 11-15 11:16 | +10 stop | ZEC | UP | 0.65 | 0.77 | 0.91 |
| 11-15 11:16 | +20 | ZEC | UP | 0.65 | open |  |
| 11-15 11:16 | +15 | ZEC | UP | 0.65 | 0.82 | 1.43 |
| 11-15 11:16 | +10 | ZEC | UP | 0.65 | 0.77 | 0.91 |
| 11-15 11:16 | +5 | ZEC | UP | 0.65 | 0.72 | 0.39 |
| 11-15 11:15 | +10 stop | ETH | UP | 0.70 | 0.83 | 1.05 |
| 11-15 11:15 | +20 | ETH | UP | 0.70 | open |  |
| 11-15 11:15 | +15 | ETH | UP | 0.69 | open |  |
| 11-15 11:15 | +10 | ETH | UP | 0.70 | 0.83 | 1.06 |
| 11-15 11:15 | +5 | ETH | UP | 0.67 | 0.75 | 0.50 |
| 11-15 11:10 | +10 stop | HYPE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-15 11:09 | +10 stop | DOGE | UP | 0.16 | 0.54 | 3.52 |
| 11-15 11:09 | +10 stop | SOL | UP | 0.71 | 0.22 | -5.18 |
| 11-15 11:09 | +10 | SOL | UP | 0.71 | no | -7.25 |
| 11-15 11:09 | +5 | SOL | UP | 0.71 | no | -7.25 |
| 11-15 11:09 | +10 stop | ETH | DOWN | 0.64 | 0.84 | 1.78 |
| 11-15 11:09 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.78 |
| 11-15 11:09 | +15 | ETH | DOWN | 0.64 | 0.84 | 1.78 |
| 11-15 11:09 | +10 | ETH | DOWN | 0.63 | 0.84 | 1.83 |
| 11-15 11:09 | +5 | ETH | DOWN | 0.64 | 0.84 | 1.78 |
| 11-15 11:09 | +10 stop | ZEC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-15 11:08 | +10 stop | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 11-15 11:08 | +20 | NEAR | DOWN | 0.67 | 0.90 | 2.08 |
| 11-15 11:08 | +15 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 11-15 11:08 | +10 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
