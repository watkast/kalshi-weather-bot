# Range-Scalp Bot

*Updated Sat Nov 14 12:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59427 | 51858 | 7569 (107) | 3 | $-16014.50 | -4.3% |
| **+10¢** | 44379 | 35518 | 8861 (142) | 3 | $-15039.94 | -5.4% |
| **+15¢** | 37192 | 27637 | 9555 (178) | 3 | $-13664.81 | -5.9% |
| **+20¢** | 33132 | 23103 | 10029 (230) | 3 | $-12039.72 | -5.8% |
| **+10¢ (15¢ stop)** | 72302 | 72160 | 142 (82) | 0 | $-26594.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 11:58 | +10 stop | NEAR | DOWN | 0.65 | 0.95 | 2.77 |
| 11-14 11:57 | +10 stop | ETH | DOWN | 0.65 | 0.77 | 0.91 |
| 11-14 11:57 | +5 | ETH | DOWN | 0.65 | 0.77 | 0.91 |
| 11-14 11:57 | +10 stop | SOL | DOWN | 0.61 | 0.75 | 1.09 |
| 11-14 11:56 | +10 stop | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-14 11:56 | +5 | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-14 11:56 | +10 stop | BTC | UP | 0.71 | 0.56 | -1.83 |
| 11-14 11:56 | +10 stop | NEAR | UP | 0.59 | 0.44 | -1.85 |
| 11-14 11:56 | +10 stop | BTC | UP | 0.55 | 0.65 | 0.66 |
| 11-14 11:54 | +10 stop | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 11:54 | +15 | BNB | DOWN | 0.62 | 0.89 | 2.46 |
| 11-14 11:54 | +10 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 11:54 | +5 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 11:53 | +10 stop | BTC | UP | 0.61 | 0.74 | 0.99 |
| 11-14 11:52 | +10 stop | BTC | UP | 0.53 | 0.64 | 0.75 |
| 11-14 11:52 | +10 stop | SOL | UP | 0.60 | 0.71 | 0.78 |
| 11-14 11:52 | +10 stop | DOGE | UP | 0.62 | 0.73 | 0.79 |
| 11-14 11:52 | +5 | DOGE | UP | 0.62 | 0.73 | 0.79 |
| 11-14 11:51 | +10 stop | HYPE | UP | 0.62 | 0.89 | 2.46 |
| 11-14 11:50 | +5 | DOGE | UP | 0.57 | 0.67 | 0.66 |
| 11-14 11:49 | +10 stop | HYPE | DOWN | 0.63 | 0.44 | -2.25 |
| 11-14 11:49 | +10 stop | BTC | UP | 0.58 | 0.68 | 0.66 |
| 11-14 11:49 | +10 stop | NEAR | UP | 0.60 | 0.72 | 0.88 |
| 11-14 11:49 | +10 stop | ETH | UP | 0.64 | 0.49 | -1.85 |
| 11-14 11:49 | +10 stop | DOGE | UP | 0.57 | 0.67 | 0.66 |
| 11-14 11:49 | +10 stop | ZEC | UP | 0.59 | 0.77 | 1.50 |
| 11-14 11:49 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 11-14 11:48 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 11-14 11:48 | +10 | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 11-14 11:48 | +5 | BNB | DOWN | 0.65 | 0.71 | 0.29 |
| 11-14 11:48 | +5 | BTC | DOWN | 0.61 | open |  |
| 11-14 11:48 | +5 | DOGE | DOWN | 0.55 | 0.62 | 0.35 |
| 11-14 11:47 | +10 stop | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-14 11:47 | +20 | XRP | UP | 0.63 | 0.90 | 2.49 |
| 11-14 11:47 | +15 | XRP | UP | 0.63 | 0.80 | 1.41 |
| 11-14 11:47 | +10 | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-14 11:47 | +5 | XRP | UP | 0.63 | 0.68 | 0.17 |
| 11-14 11:47 | +5 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 11-14 11:47 | +5 | ZEC | DOWN | 0.65 | open |  |
| 11-14 11:47 | +5 | HYPE | DOWN | 0.66 | open |  |
