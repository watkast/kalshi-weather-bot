# Range-Scalp Bot

*Updated Thu Oct 15 22:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 18243 | 15835 | 2408 (28) | 1 | $-5611.86 | -4.9% |
| **+10¢** | 13775 | 10989 | 2786 (40) | 2 | $-5064.42 | -5.8% |
| **+15¢** | 11554 | 8557 | 2997 (59) | 2 | $-4581.63 | -6.3% |
| **+20¢** | 10262 | 7130 | 3132 (78) | 4 | $-3974.04 | -6.2% |
| **+10¢ (15¢ stop)** | 22452 | 22402 | 50 (29) | 0 | $-8691.77 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 22:27 | +10 stop | SOL | UP | 0.39 | 0.57 | 1.45 |
| 10-15 22:26 | +10 stop | SOL | DOWN | 0.55 | 0.34 | -2.43 |
| 10-15 22:26 | +5 | SOL | DOWN | 0.54 | open |  |
| 10-15 22:26 | +10 stop | XRP | UP | 0.70 | 0.83 | 1.05 |
| 10-15 22:26 | +15 | XRP | UP | 0.69 | 0.90 | 1.91 |
| 10-15 22:26 | +10 | XRP | UP | 0.69 | 0.83 | 1.15 |
| 10-15 22:26 | +5 | XRP | UP | 0.69 | 0.83 | 1.15 |
| 10-15 22:24 | +5 | NEAR | DOWN | 0.53 | 0.64 | 0.75 |
| 10-15 22:24 | +10 stop | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 10-15 22:24 | +20 | NEAR | DOWN | 0.57 | 0.78 | 1.79 |
| 10-15 22:24 | +15 | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 10-15 22:24 | +10 | NEAR | DOWN | 0.57 | 0.72 | 1.17 |
| 10-15 22:24 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 10-15 22:24 | +10 stop | SOL | UP | 0.61 | 0.72 | 0.77 |
| 10-15 22:23 | +10 stop | BNB | UP | 0.69 | 0.83 | 1.15 |
| 10-15 22:23 | +5 | BNB | UP | 0.69 | 0.76 | 0.42 |
| 10-15 22:23 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-15 22:23 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 10-15 22:23 | +15 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 10-15 22:23 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.70 |
| 10-15 22:23 | +5 | ETH | DOWN | 0.63 | 0.73 | 0.70 |
| 10-15 22:22 | +10 stop | SOL | DOWN | 0.63 | 0.44 | -2.25 |
| 10-15 22:22 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-15 22:22 | +15 | SOL | DOWN | 0.63 | open |  |
| 10-15 22:22 | +10 | SOL | DOWN | 0.63 | open |  |
| 10-15 22:22 | +5 | SOL | DOWN | 0.63 | 0.70 | 0.38 |
| 10-15 22:22 | +10 stop | DOGE | DOWN | 0.44 | 0.56 | 0.84 |
| 10-15 22:22 | +10 stop | XRP | DOWN | 0.44 | 0.61 | 1.35 |
| 10-15 22:22 | +15 | XRP | DOWN | 0.44 | 0.61 | 1.35 |
| 10-15 22:22 | +10 | XRP | DOWN | 0.44 | 0.61 | 1.35 |
| 10-15 22:22 | +5 | XRP | DOWN | 0.43 | 0.61 | 1.45 |
| 10-15 22:22 | +5 | BNB | DOWN | 0.45 | 0.58 | 0.94 |
| 10-15 22:22 | +10 stop | HYPE | DOWN | 0.64 | 0.42 | -2.59 |
| 10-15 22:22 | +10 stop | DOGE | DOWN | 0.71 | 0.54 | -2.03 |
| 10-15 22:22 | +10 stop | BTC | DOWN | 0.38 | 0.54 | 1.25 |
| 10-15 22:22 | +15 | BTC | DOWN | 0.38 | 0.54 | 1.25 |
| 10-15 22:22 | +10 | BTC | DOWN | 0.38 | 0.54 | 1.25 |
| 10-15 22:22 | +5 | BTC | DOWN | 0.38 | 0.54 | 1.25 |
| 10-15 22:18 | +10 stop | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 10-15 22:17 | +10 stop | XRP | DOWN | 0.68 | 0.79 | 0.82 |
