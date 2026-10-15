# Range-Scalp Bot

*Updated Thu Oct 15 18:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 17941 | 15570 | 2371 (28) | 7 | $-5532.17 | -4.9% |
| **+10¢** | 13551 | 10805 | 2746 (40) | 8 | $-5030.99 | -5.9% |
| **+15¢** | 11365 | 8413 | 2952 (59) | 8 | $-4532.73 | -6.4% |
| **+20¢** | 10102 | 7014 | 3088 (77) | 8 | $-3950.68 | -6.2% |
| **+10¢ (15¢ stop)** | 22102 | 22052 | 50 (29) | 3 | $-8562.75 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 18:24 | +10 stop | XRP | UP | 0.67 | open |  |
| 10-15 18:24 | +20 | XRP | UP | 0.67 | open |  |
| 10-15 18:24 | +15 | XRP | UP | 0.67 | open |  |
| 10-15 18:24 | +10 | XRP | UP | 0.67 | open |  |
| 10-15 18:24 | +5 | XRP | UP | 0.67 | open |  |
| 10-15 18:24 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 10-15 18:23 | +10 stop | DOGE | DOWN | 0.63 | open |  |
| 10-15 18:23 | +10 stop | ETH | UP | 0.54 | 0.38 | -1.95 |
| 10-15 18:21 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 10-15 18:21 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-15 18:21 | +10 stop | BTC | DOWN | 0.60 | 0.70 | 0.68 |
| 10-15 18:21 | +10 stop | ETH | DOWN | 0.59 | 0.42 | -2.05 |
| 10-15 18:20 | +10 stop | XRP | UP | 0.68 | 0.52 | -1.94 |
| 10-15 18:20 | +10 | XRP | UP | 0.68 | 0.84 | 1.34 |
| 10-15 18:20 | +5 | XRP | UP | 0.66 | 0.84 | 1.54 |
| 10-15 18:19 | +15 | NEAR | UP | 0.67 | 0.85 | 1.55 |
| 10-15 18:18 | +5 | BTC | UP | 0.64 | open |  |
| 10-15 18:18 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-15 18:18 | +10 | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-15 18:17 | +5 | NEAR | UP | 0.71 | 0.77 | 0.32 |
| 10-15 18:17 | +5 | XRP | UP | 0.57 | 0.63 | 0.25 |
| 10-15 18:17 | +10 stop | ZEC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-15 18:16 | +5 | SOL | DOWN | 0.58 | 0.65 | 0.36 |
| 10-15 18:16 | +10 stop | HYPE | UP | 0.69 | 0.52 | -2.03 |
| 10-15 18:16 | +20 | HYPE | UP | 0.69 | open |  |
| 10-15 18:16 | +15 | HYPE | UP | 0.69 | open |  |
| 10-15 18:16 | +10 | HYPE | UP | 0.69 | open |  |
| 10-15 18:16 | +5 | HYPE | UP | 0.69 | open |  |
| 10-15 18:16 | +10 stop | SOL | UP | 0.50 | 0.34 | -1.94 |
| 10-15 18:16 | +20 | SOL | UP | 0.50 | open |  |
| 10-15 18:16 | +15 | SOL | UP | 0.50 | open |  |
| 10-15 18:16 | +10 | SOL | UP | 0.50 | open |  |
| 10-15 18:16 | +5 | SOL | UP | 0.50 | 0.56 | 0.24 |
| 10-15 18:16 | +10 stop | DOGE | UP | 0.54 | 0.39 | -1.85 |
| 10-15 18:16 | +20 | DOGE | UP | 0.54 | open |  |
| 10-15 18:16 | +15 | DOGE | UP | 0.54 | open |  |
| 10-15 18:16 | +10 | DOGE | UP | 0.55 | open |  |
| 10-15 18:16 | +5 | DOGE | UP | 0.55 | open |  |
| 10-15 18:16 | +10 stop | NEAR | UP | 0.55 | 0.67 | 0.86 |
| 10-15 18:16 | +20 | NEAR | UP | 0.55 | 0.77 | 1.89 |
