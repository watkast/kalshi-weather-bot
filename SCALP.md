# Range-Scalp Bot

*Updated Sun Nov 22 03:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68206 | 59523 | 8683 (138) | 2 | $-18320.28 | -4.3% |
| **+10¢** | 50926 | 40784 | 10142 (181) | 2 | $-16990.29 | -5.3% |
| **+15¢** | 42687 | 31754 | 10933 (231) | 3 | $-15235.24 | -5.7% |
| **+20¢** | 38002 | 26512 | 11490 (289) | 3 | $-13557.78 | -5.7% |
| **+10¢ (15¢ stop)** | 83053 | 82874 | 179 (111) | 0 | $-30500.49 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 03:36 | +10 stop | XRP | DOWN | 0.64 | 0.75 | 0.75 |
| 11-22 03:36 | +5 | XRP | DOWN | 0.64 | 0.75 | 0.74 |
| 11-22 03:35 | +5 | XRP | DOWN | 0.63 | 0.71 | 0.48 |
| 11-22 03:34 | +10 stop | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 11-22 03:34 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-22 03:34 | +10 | NEAR | DOWN | 0.65 | 0.75 | 0.70 |
| 11-22 03:34 | +5 | NEAR | DOWN | 0.65 | 0.73 | 0.50 |
| 11-22 03:34 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 11-22 03:34 | +10 stop | XRP | DOWN | 0.57 | 0.71 | 1.07 |
| 11-22 03:34 | +5 | XRP | DOWN | 0.57 | 0.63 | 0.23 |
| 11-22 03:33 | +10 stop | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 11-22 03:33 | +5 | ETH | DOWN | 0.66 | 0.76 | 0.71 |
| 11-22 03:33 | +10 stop | ZEC | DOWN | 0.64 | 0.40 | -2.74 |
| 11-22 03:32 | +10 stop | XRP | UP | 0.59 | 0.44 | -1.85 |
| 11-22 03:32 | +5 | XRP | UP | 0.62 | 0.68 | 0.27 |
| 11-22 03:32 | +10 stop | HYPE | UP | 0.56 | 0.40 | -1.95 |
| 11-22 03:32 | +20 | HYPE | UP | 0.56 | open |  |
| 11-22 03:32 | +15 | HYPE | UP | 0.56 | open |  |
| 11-22 03:32 | +10 | HYPE | UP | 0.56 | open |  |
| 11-22 03:32 | +5 | HYPE | UP | 0.56 | open |  |
| 11-22 03:32 | +5 | ZEC | UP | 0.58 | open |  |
| 11-22 03:32 | +10 | XRP | UP | 0.67 | open |  |
| 11-22 03:32 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-22 03:32 | +20 | BTC | DOWN | 0.61 | 0.83 | 1.93 |
| 11-22 03:32 | +15 | BTC | DOWN | 0.61 | 0.79 | 1.51 |
| 11-22 03:32 | +10 | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-22 03:32 | +5 | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-22 03:31 | +10 stop | SOL | DOWN | 0.57 | 0.73 | 1.28 |
| 11-22 03:31 | +20 | SOL | DOWN | 0.58 | 0.80 | 1.90 |
| 11-22 03:31 | +15 | SOL | DOWN | 0.59 | 0.75 | 1.29 |
| 11-22 03:31 | +10 | SOL | DOWN | 0.59 | 0.73 | 1.09 |
| 11-22 03:31 | +5 | SOL | DOWN | 0.59 | 0.73 | 1.09 |
| 11-22 03:31 | +10 stop | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 11-22 03:31 | +20 | NEAR | DOWN | 0.58 | 0.78 | 1.69 |
| 11-22 03:31 | +15 | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 11-22 03:31 | +10 | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 11-22 03:31 | +5 | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 11-22 03:31 | +5 | XRP | UP | 0.62 | 0.69 | 0.38 |
| 11-22 03:31 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-22 03:31 | +20 | ETH | DOWN | 0.58 | 0.79 | 1.80 |
