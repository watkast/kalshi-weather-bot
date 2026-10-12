# Range-Scalp Bot

*Updated Mon Oct 12 00:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 12749 | 11006 | 1743 (25) | 7 | $-4203.10 | -5.2% |
| **+10¢** | 9669 | 7654 | 2015 (37) | 8 | $-3916.09 | -6.4% |
| **+15¢** | 8134 | 5988 | 2146 (55) | 9 | $-3400.86 | -6.7% |
| **+20¢** | 7248 | 5010 | 2238 (69) | 9 | $-2905.22 | -6.4% |
| **+10¢ (15¢ stop)** | 15726 | 15685 | 41 (25) | 6 | $-6164.36 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-12 00:37 | +20 | SOL | DOWN | 0.59 | open |  |
| 10-12 00:37 | +15 | SOL | DOWN | 0.59 | open |  |
| 10-12 00:37 | +10 stop | ETH | DOWN | 0.50 | open |  |
| 10-12 00:37 | +10 stop | BNB | DOWN | 0.54 | open |  |
| 10-12 00:37 | +10 stop | SOL | DOWN | 0.63 | open |  |
| 10-12 00:36 | +10 stop | BTC | UP | 0.54 | open |  |
| 10-12 00:36 | +10 stop | ETH | UP | 0.57 | 0.42 | -1.86 |
| 10-12 00:36 | +5 | DOGE | DOWN | 0.67 | 0.76 | 0.61 |
| 10-12 00:35 | +10 stop | BTC | DOWN | 0.61 | 0.42 | -2.25 |
| 10-12 00:34 | +10 stop | SOL | UP | 0.70 | 0.49 | -2.43 |
| 10-12 00:34 | +10 stop | ZEC | UP | 0.65 | 0.46 | -2.24 |
| 10-12 00:34 | +5 | NEAR | UP | 0.62 | 0.67 | 0.17 |
| 10-12 00:33 | +10 stop | DOGE | DOWN | 0.70 | open |  |
| 10-12 00:33 | +10 stop | NEAR | UP | 0.55 | 0.67 | 0.86 |
| 10-12 00:33 | +5 | NEAR | UP | 0.55 | 0.64 | 0.55 |
| 10-12 00:33 | +10 stop | SOL | UP | 0.69 | 0.50 | -2.23 |
| 10-12 00:33 | +10 | SOL | UP | 0.69 | open |  |
| 10-12 00:33 | +5 | SOL | UP | 0.69 | open |  |
| 10-12 00:33 | +10 stop | HYPE | UP | 0.61 | 0.45 | -1.99 |
| 10-12 00:33 | +20 | HYPE | UP | 0.61 | open |  |
| 10-12 00:33 | +15 | HYPE | UP | 0.61 | open |  |
| 10-12 00:33 | +10 | HYPE | UP | 0.61 | open |  |
| 10-12 00:33 | +5 | HYPE | UP | 0.61 | open |  |
| 10-12 00:33 | +10 stop | BNB | UP | 0.60 | 0.38 | -2.54 |
| 10-12 00:33 | +10 stop | BTC | UP | 0.65 | 0.44 | -2.44 |
| 10-12 00:32 | +10 stop | ETH | UP | 0.71 | 0.50 | -2.43 |
| 10-12 00:32 | +5 | ETH | UP | 0.71 | open |  |
| 10-12 00:32 | +10 stop | DOGE | UP | 0.68 | 0.50 | -2.14 |
| 10-12 00:32 | +10 stop | XRP | UP | 0.70 | open |  |
| 10-12 00:32 | +10 stop | SOL | DOWN | 0.41 | 0.55 | 1.05 |
| 10-12 00:32 | +20 | SOL | DOWN | 0.41 | 0.61 | 1.66 |
| 10-12 00:32 | +15 | SOL | DOWN | 0.41 | 0.61 | 1.66 |
| 10-12 00:32 | +10 | SOL | DOWN | 0.41 | 0.55 | 1.05 |
| 10-12 00:32 | +5 | SOL | DOWN | 0.41 | 0.55 | 1.05 |
| 10-12 00:32 | +5 | NEAR | DOWN | 0.52 | 0.60 | 0.45 |
| 10-12 00:30 | +10 stop | BNB | DOWN | 0.60 | 0.41 | -2.24 |
| 10-12 00:30 | +20 | BNB | DOWN | 0.60 | open |  |
| 10-12 00:30 | +15 | BNB | DOWN | 0.60 | open |  |
| 10-12 00:30 | +10 | BNB | DOWN | 0.60 | open |  |
| 10-12 00:30 | +5 | BNB | DOWN | 0.60 | open |  |
