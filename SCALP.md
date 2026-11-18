# Range-Scalp Bot

*Updated Wed Nov 18 22:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64405 | 56177 | 8228 (124) | 3 | $-17555.47 | -4.3% |
| **+10¢** | 48111 | 38488 | 9623 (165) | 3 | $-16373.93 | -5.4% |
| **+15¢** | 40336 | 29965 | 10371 (210) | 3 | $-14792.69 | -5.8% |
| **+20¢** | 35917 | 25030 | 10887 (265) | 3 | $-13086.76 | -5.8% |
| **+10¢ (15¢ stop)** | 78353 | 78189 | 164 (98) | 1 | $-28853.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 22:42 | +10 stop | BTC | DOWN | 0.69 | 0.39 | -3.32 |
| 11-18 22:42 | +10 | BTC | DOWN | 0.69 | open |  |
| 11-18 22:42 | +5 | BTC | DOWN | 0.67 | open |  |
| 11-18 22:42 | +10 stop | NEAR | UP | 0.67 | open |  |
| 11-18 22:42 | +20 | NEAR | UP | 0.67 | open |  |
| 11-18 22:42 | +15 | NEAR | UP | 0.67 | open |  |
| 11-18 22:42 | +10 | NEAR | UP | 0.67 | open |  |
| 11-18 22:42 | +5 | NEAR | UP | 0.67 | open |  |
| 11-18 22:41 | +10 stop | BTC | UP | 0.46 | 0.56 | 0.64 |
| 11-18 22:41 | +20 | BTC | UP | 0.46 | 0.84 | 3.52 |
| 11-18 22:41 | +15 | BTC | UP | 0.46 | 0.61 | 1.15 |
| 11-18 22:41 | +10 | BTC | UP | 0.46 | 0.56 | 0.64 |
| 11-18 22:41 | +5 | BTC | UP | 0.45 | 0.56 | 0.74 |
| 11-18 22:41 | +10 stop | SOL | DOWN | 0.68 | 0.52 | -1.94 |
| 11-18 22:41 | +20 | SOL | DOWN | 0.68 | open |  |
| 11-18 22:41 | +15 | SOL | DOWN | 0.68 | open |  |
| 11-18 22:41 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-18 22:41 | +5 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-18 22:40 | +5 | ZEC | DOWN | 0.70 | 0.79 | 0.63 |
| 11-18 22:40 | +10 stop | DOGE | DOWN | 0.71 | 0.91 | 1.85 |
| 11-18 22:40 | +10 stop | XRP | UP | 0.61 | 0.27 | -3.76 |
| 11-18 22:40 | +20 | XRP | UP | 0.61 | open |  |
| 11-18 22:40 | +15 | XRP | UP | 0.61 | open |  |
| 11-18 22:40 | +10 | XRP | UP | 0.61 | open |  |
| 11-18 22:40 | +5 | XRP | UP | 0.61 | open |  |
| 11-18 22:40 | +10 stop | DOGE | UP | 0.33 | 0.64 | 2.77 |
| 11-18 22:39 | +10 stop | DOGE | DOWN | 0.40 | 0.58 | 1.45 |
| 11-18 22:39 | +10 stop | ZEC | DOWN | 0.65 | 0.79 | 1.12 |
| 11-18 22:38 | +10 stop | XRP | UP | 0.64 | 0.74 | 0.69 |
| 11-18 22:37 | +10 stop | ZEC | UP | 0.53 | 0.38 | -1.85 |
| 11-18 22:37 | +10 stop | XRP | UP | 0.69 | 0.52 | -2.03 |
| 11-18 22:37 | +10 | XRP | UP | 0.69 | 0.79 | 0.73 |
| 11-18 22:37 | +10 stop | DOGE | UP | 0.66 | 0.45 | -2.44 |
| 11-18 22:36 | +10 stop | ZEC | DOWN | 0.59 | 0.40 | -2.24 |
| 11-18 22:36 | +10 stop | XRP | UP | 0.54 | 0.66 | 0.86 |
| 11-18 22:36 | +10 | XRP | UP | 0.55 | 0.66 | 0.76 |
| 11-18 22:35 | +10 stop | DOGE | UP | 0.65 | 0.45 | -2.34 |
| 11-18 22:35 | +10 stop | NEAR | UP | 0.70 | 0.84 | 1.15 |
| 11-18 22:35 | +20 | NEAR | UP | 0.70 | 0.91 | 1.89 |
| 11-18 22:35 | +15 | NEAR | UP | 0.70 | 0.89 | 1.68 |
