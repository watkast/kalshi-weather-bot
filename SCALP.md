# Range-Scalp Bot

*Updated Thu Oct 15 15:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17727 | 15386 | 2341 (28) | 7 | $-5447.56 | -4.9% |
| **+10¢** | 13394 | 10683 | 2711 (40) | 7 | $-4939.04 | -5.9% |
| **+15¢** | 11237 | 8325 | 2912 (59) | 8 | $-4415.31 | -6.3% |
| **+20¢** | 9991 | 6944 | 3047 (77) | 8 | $-3837.86 | -6.1% |
| **+10¢ (15¢ stop)** | 21846 | 21796 | 50 (29) | 0 | $-8464.50 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 15:39 | +10 stop | XRP | UP | 0.65 | 0.86 | 1.85 |
| 10-15 15:38 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.95 |
| 10-15 15:38 | +5 | XRP | DOWN | 0.63 | 0.82 | 1.62 |
| 10-15 15:37 | +10 stop | XRP | DOWN | 0.44 | 0.57 | 0.94 |
| 10-15 15:37 | +5 | XRP | DOWN | 0.52 | 0.57 | 0.14 |
| 10-15 15:37 | +10 stop | DOGE | UP | 0.71 | 0.83 | 0.95 |
| 10-15 15:36 | +10 stop | ZEC | UP | 0.66 | 0.81 | 1.23 |
| 10-15 15:36 | +10 stop | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-15 15:36 | +15 | HYPE | UP | 0.67 | 0.86 | 1.65 |
| 10-15 15:36 | +10 | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-15 15:36 | +5 | HYPE | UP | 0.67 | 0.77 | 0.71 |
| 10-15 15:36 | +10 stop | NEAR | UP | 0.63 | 0.73 | 0.69 |
| 10-15 15:36 | +10 stop | XRP | UP | 0.61 | 0.43 | -2.17 |
| 10-15 15:36 | +5 | XRP | UP | 0.61 | 0.66 | 0.17 |
| 10-15 15:36 | +10 stop | BTC | UP | 0.69 | 0.84 | 1.25 |
| 10-15 15:35 | +10 stop | SOL | UP | 0.71 | 0.84 | 1.05 |
| 10-15 15:35 | +10 stop | ZEC | UP | 0.63 | 0.76 | 1.00 |
| 10-15 15:35 | +10 stop | BNB | UP | 0.66 | 0.80 | 1.12 |
| 10-15 15:34 | +10 stop | DOGE | UP | 0.58 | 0.76 | 1.49 |
| 10-15 15:34 | +10 stop | ETH | UP | 0.62 | 0.74 | 0.89 |
| 10-15 15:34 | +10 stop | NEAR | UP | 0.63 | 0.83 | 1.75 |
| 10-15 15:34 | +5 | XRP | DOWN | 0.55 | 0.64 | 0.55 |
| 10-15 15:33 | +5 | HYPE | UP | 0.64 | 0.75 | 0.75 |
| 10-15 15:32 | +10 stop | HYPE | UP | 0.61 | 0.75 | 1.09 |
| 10-15 15:32 | +20 | HYPE | UP | 0.61 | 0.86 | 2.24 |
| 10-15 15:32 | +15 | HYPE | UP | 0.61 | 0.76 | 1.20 |
| 10-15 15:32 | +10 | HYPE | UP | 0.61 | 0.75 | 1.09 |
| 10-15 15:32 | +5 | HYPE | UP | 0.61 | 0.68 | 0.37 |
| 10-15 15:32 | +5 | NEAR | DOWN | 0.65 | open |  |
| 10-15 15:31 | +10 stop | XRP | DOWN | 0.71 | 0.51 | -2.33 |
| 10-15 15:31 | +20 | XRP | DOWN | 0.71 | open |  |
| 10-15 15:31 | +15 | XRP | DOWN | 0.71 | open |  |
| 10-15 15:31 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-15 15:31 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 10-15 15:31 | +10 stop | ZEC | DOWN | 0.66 | 0.51 | -1.84 |
| 10-15 15:31 | +20 | ZEC | DOWN | 0.66 | open |  |
| 10-15 15:31 | +15 | ZEC | DOWN | 0.65 | open |  |
| 10-15 15:31 | +10 | ZEC | DOWN | 0.65 | open |  |
| 10-15 15:31 | +5 | ZEC | DOWN | 0.64 | open |  |
| 10-15 15:31 | +10 stop | BNB | DOWN | 0.61 | 0.42 | -2.25 |
