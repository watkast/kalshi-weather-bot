# Range-Scalp Bot

*Updated Thu Nov 12 21:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57303 | 49963 | 7340 (101) | 5 | $-15700.43 | -4.4% |
| **+10¢** | 42829 | 34263 | 8566 (133) | 6 | $-14625.69 | -5.4% |
| **+15¢** | 35906 | 26685 | 9221 (167) | 7 | $-13226.30 | -5.9% |
| **+20¢** | 31991 | 22316 | 9675 (217) | 7 | $-11584.16 | -5.8% |
| **+10¢ (15¢ stop)** | 69874 | 69746 | 128 (78) | 0 | $-25766.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 21:20 | +10 stop | ZEC | DOWN | 0.58 | 0.80 | 1.90 |
| 11-12 21:19 | +10 stop | ETH | UP | 0.68 | 0.49 | -2.24 |
| 11-12 21:19 | +10 | ETH | UP | 0.69 | open |  |
| 11-12 21:19 | +5 | ETH | UP | 0.69 | open |  |
| 11-12 21:19 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-12 21:19 | +10 stop | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 11-12 21:18 | +5 | SOL | UP | 0.66 | open |  |
| 11-12 21:17 | +5 | ZEC | UP | 0.59 | open |  |
| 11-12 21:17 | +5 | ZEC | UP | 0.56 | 0.64 | 0.45 |
| 11-12 21:16 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
| 11-12 21:16 | +20 | NEAR | UP | 0.64 | open |  |
| 11-12 21:16 | +15 | NEAR | UP | 0.64 | open |  |
| 11-12 21:16 | +10 | NEAR | UP | 0.64 | open |  |
| 11-12 21:16 | +5 | NEAR | UP | 0.64 | open |  |
| 11-12 21:16 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-12 21:16 | +20 | XRP | UP | 0.69 | 0.90 | 1.89 |
| 11-12 21:16 | +15 | XRP | UP | 0.70 | 0.85 | 1.26 |
| 11-12 21:16 | +10 | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-12 21:16 | +5 | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-12 21:16 | +10 stop | SOL | UP | 0.64 | 0.36 | -3.14 |
| 11-12 21:16 | +20 | SOL | UP | 0.64 | open |  |
| 11-12 21:16 | +15 | SOL | UP | 0.64 | open |  |
| 11-12 21:16 | +10 | SOL | UP | 0.64 | open |  |
| 11-12 21:16 | +5 | SOL | UP | 0.64 | 0.69 | 0.18 |
| 11-12 21:16 | +10 | DOGE | UP | 0.71 | open |  |
| 11-12 21:15 | +10 stop | ZEC | UP | 0.58 | 0.42 | -1.96 |
| 11-12 21:15 | +20 | ZEC | UP | 0.58 | open |  |
| 11-12 21:15 | +15 | ZEC | UP | 0.58 | open |  |
| 11-12 21:15 | +10 | ZEC | UP | 0.58 | open |  |
| 11-12 21:15 | +5 | ZEC | UP | 0.58 | 0.63 | 0.15 |
| 11-12 21:15 | +10 stop | ETH | UP | 0.67 | 0.78 | 0.81 |
| 11-12 21:15 | +20 | ETH | UP | 0.67 | open |  |
| 11-12 21:15 | +15 | ETH | UP | 0.67 | open |  |
| 11-12 21:15 | +10 | ETH | UP | 0.67 | 0.78 | 0.81 |
| 11-12 21:15 | +5 | ETH | UP | 0.67 | 0.72 | 0.19 |
| 11-12 21:15 | +10 stop | HYPE | UP | 0.58 | 0.42 | -1.96 |
| 11-12 21:15 | +20 | HYPE | UP | 0.58 | open |  |
| 11-12 21:15 | +15 | HYPE | UP | 0.57 | open |  |
| 11-12 21:15 | +10 | HYPE | UP | 0.57 | open |  |
| 11-12 21:15 | +5 | HYPE | UP | 0.57 | open |  |
