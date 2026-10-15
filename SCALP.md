# Range-Scalp Bot

*Updated Thu Oct 15 10:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17342 | 15057 | 2285 (28) | 4 | $-5259.82 | -4.8% |
| **+10¢** | 13105 | 10457 | 2648 (40) | 3 | $-4781.32 | -5.8% |
| **+15¢** | 11009 | 8165 | 2844 (59) | 3 | $-4237.52 | -6.1% |
| **+20¢** | 9781 | 6806 | 2975 (77) | 3 | $-3670.33 | -6.0% |
| **+10¢ (15¢ stop)** | 21321 | 21271 | 50 (29) | 2 | $-8242.16 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 10:21 | +10 stop | ETH | DOWN | 0.69 | open |  |
| 10-15 10:21 | +10 stop | DOGE | DOWN | 0.68 | open |  |
| 10-15 10:20 | +5 | ETH | UP | 0.57 | open |  |
| 10-15 10:20 | +10 stop | NEAR | DOWN | 0.65 | 0.76 | 0.81 |
| 10-15 10:20 | +10 stop | BNB | UP | 0.62 | 0.43 | -2.25 |
| 10-15 10:20 | +10 stop | ETH | UP | 0.59 | 0.40 | -2.24 |
| 10-15 10:20 | +20 | ETH | UP | 0.59 | open |  |
| 10-15 10:20 | +15 | ETH | UP | 0.59 | open |  |
| 10-15 10:20 | +10 | ETH | UP | 0.59 | open |  |
| 10-15 10:20 | +5 | ETH | UP | 0.59 | 0.66 | 0.37 |
| 10-15 10:20 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-15 10:20 | +20 | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 10-15 10:20 | +15 | SOL | DOWN | 0.64 | 0.79 | 1.21 |
| 10-15 10:20 | +10 | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-15 10:20 | +5 | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-15 10:20 | +10 stop | DOGE | UP | 0.66 | 0.47 | -2.24 |
| 10-15 10:20 | +20 | DOGE | UP | 0.66 | open |  |
| 10-15 10:20 | +15 | DOGE | UP | 0.66 | open |  |
| 10-15 10:20 | +10 | DOGE | UP | 0.66 | open |  |
| 10-15 10:20 | +5 | DOGE | UP | 0.66 | open |  |
| 10-15 10:20 | +10 stop | XRP | UP | 0.61 | 0.36 | -2.84 |
| 10-15 10:20 | +5 | XRP | UP | 0.61 | open |  |
| 10-15 10:19 | +5 | ZEC | UP | 0.48 | open |  |
| 10-15 10:19 | +10 stop | ZEC | UP | 0.51 | 0.27 | -2.72 |
| 10-15 10:19 | +20 | ZEC | UP | 0.51 | open |  |
| 10-15 10:19 | +15 | ZEC | UP | 0.51 | open |  |
| 10-15 10:19 | +10 | ZEC | UP | 0.51 | open |  |
| 10-15 10:19 | +5 | ZEC | UP | 0.51 | 0.56 | 0.14 |
| 10-15 10:18 | +10 stop | NEAR | UP | 0.56 | 0.32 | -2.74 |
| 10-15 10:17 | +5 | XRP | UP | 0.68 | 0.87 | 1.66 |
| 10-15 10:17 | +10 stop | ETH | UP | 0.56 | 0.72 | 1.27 |
| 10-15 10:17 | +20 | ETH | UP | 0.56 | 0.85 | 2.63 |
| 10-15 10:17 | +15 | ETH | UP | 0.56 | 0.72 | 1.27 |
| 10-15 10:17 | +10 | ETH | UP | 0.56 | 0.72 | 1.27 |
| 10-15 10:17 | +5 | ETH | UP | 0.56 | 0.62 | 0.25 |
| 10-15 10:16 | +10 stop | DOGE | UP | 0.56 | 0.78 | 1.89 |
| 10-15 10:16 | +20 | DOGE | UP | 0.55 | 0.78 | 1.98 |
| 10-15 10:16 | +15 | DOGE | UP | 0.55 | 0.78 | 1.98 |
| 10-15 10:16 | +10 | DOGE | UP | 0.55 | 0.78 | 1.97 |
| 10-15 10:16 | +5 | DOGE | UP | 0.55 | 0.62 | 0.33 |
