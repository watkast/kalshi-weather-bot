# Range-Scalp Bot

*Updated Wed Nov 11 00:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55115 | 48072 | 7043 (94) | 4 | $-15019.33 | -4.3% |
| **+10¢** | 41183 | 32971 | 8212 (124) | 5 | $-13901.06 | -5.4% |
| **+15¢** | 34525 | 25674 | 8851 (158) | 5 | $-12632.40 | -5.8% |
| **+20¢** | 30736 | 21450 | 9286 (207) | 4 | $-11038.92 | -5.7% |
| **+10¢ (15¢ stop)** | 67147 | 67029 | 118 (73) | 0 | $-24769.15 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 00:25 | +10 stop | ETH | DOWN | 0.60 | 0.72 | 0.88 |
| 11-11 00:25 | +20 | ETH | DOWN | 0.60 | 0.82 | 1.92 |
| 11-11 00:25 | +15 | ETH | DOWN | 0.60 | 0.76 | 1.30 |
| 11-11 00:25 | +10 | ETH | DOWN | 0.60 | 0.72 | 0.88 |
| 11-11 00:25 | +5 | ETH | DOWN | 0.60 | 0.72 | 0.88 |
| 11-11 00:25 | +10 stop | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 11-11 00:24 | +10 stop | XRP | UP | 0.63 | 0.81 | 1.52 |
| 11-11 00:24 | +5 | SOL | UP | 0.54 | 0.61 | 0.35 |
| 11-11 00:23 | +10 stop | BNB | DOWN | 0.57 | 0.67 | 0.66 |
| 11-11 00:23 | +10 stop | XRP | DOWN | 0.57 | 0.42 | -1.86 |
| 11-11 00:23 | +5 | XRP | DOWN | 0.56 | open |  |
| 11-11 00:23 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-11 00:23 | +10 stop | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-11 00:22 | +5 | HYPE | DOWN | 0.64 | 0.83 | 1.63 |
| 11-11 00:22 | +10 stop | SOL | UP | 0.51 | 0.61 | 0.65 |
| 11-11 00:22 | +10 | SOL | UP | 0.51 | 0.61 | 0.65 |
| 11-11 00:22 | +5 | SOL | UP | 0.51 | 0.59 | 0.45 |
| 11-11 00:22 | +10 stop | ETH | DOWN | 0.65 | 0.77 | 0.91 |
| 11-11 00:21 | +10 stop | XRP | DOWN | 0.58 | 0.72 | 1.07 |
| 11-11 00:21 | +10 stop | DOGE | DOWN | 0.52 | 0.68 | 1.26 |
| 11-11 00:21 | +10 stop | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-11 00:20 | +10 stop | HYPE | UP | 0.55 | 0.38 | -2.05 |
| 11-11 00:20 | +10 | HYPE | UP | 0.55 | open |  |
| 11-11 00:20 | +5 | HYPE | UP | 0.55 | 0.60 | 0.15 |
| 11-11 00:20 | +10 stop | SOL | UP | 0.60 | 0.74 | 1.09 |
| 11-11 00:20 | +15 | SOL | UP | 0.60 | 0.76 | 1.30 |
| 11-11 00:20 | +10 | SOL | UP | 0.61 | 0.74 | 0.99 |
| 11-11 00:20 | +5 | SOL | UP | 0.61 | 0.67 | 0.27 |
| 11-11 00:20 | +10 stop | BNB | UP | 0.52 | 0.36 | -1.95 |
| 11-11 00:20 | +15 | BNB | UP | 0.53 | open |  |
| 11-11 00:20 | +10 | BNB | UP | 0.53 | open |  |
| 11-11 00:20 | +5 | BNB | UP | 0.53 | open |  |
| 11-11 00:19 | +10 stop | ETH | UP | 0.58 | 0.43 | -1.86 |
| 11-11 00:19 | +10 stop | XRP | UP | 0.61 | 0.36 | -2.84 |
| 11-11 00:19 | +5 | DOGE | UP | 0.57 | open |  |
| 11-11 00:18 | +10 stop | DOGE | UP | 0.58 | 0.38 | -2.35 |
| 11-11 00:18 | +20 | DOGE | UP | 0.58 | open |  |
| 11-11 00:18 | +15 | DOGE | UP | 0.58 | open |  |
| 11-11 00:18 | +10 | DOGE | UP | 0.58 | open |  |
| 11-11 00:18 | +5 | DOGE | UP | 0.58 | 0.65 | 0.36 |
