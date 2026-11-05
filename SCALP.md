# Range-Scalp Bot

*Updated Thu Nov 05 12:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48273 | 42053 | 6220 (73) | 3 | $-13801.65 | -4.5% |
| **+10¢** | 36046 | 28821 | 7225 (99) | 2 | $-12651.30 | -5.6% |
| **+15¢** | 30205 | 22425 | 7780 (127) | 4 | $-11549.85 | -6.1% |
| **+20¢** | 26832 | 18682 | 8150 (166) | 4 | $-10202.15 | -6.1% |
| **+10¢ (15¢ stop)** | 58819 | 58726 | 93 (56) | 1 | $-21845.38 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 12:57 | +10 stop | DOGE | UP | 0.52 | open |  |
| 11-05 12:57 | +20 | DOGE | UP | 0.52 | open |  |
| 11-05 12:57 | +15 | DOGE | UP | 0.52 | open |  |
| 11-05 12:57 | +10 | DOGE | UP | 0.51 | 0.61 | 0.65 |
| 11-05 12:57 | +5 | DOGE | UP | 0.51 | 0.61 | 0.65 |
| 11-05 12:57 | +10 stop | SOL | UP | 0.52 | 0.62 | 0.65 |
| 11-05 12:57 | +10 | SOL | UP | 0.52 | 0.62 | 0.65 |
| 11-05 12:56 | +10 stop | XRP | UP | 0.65 | 0.49 | -1.94 |
| 11-05 12:56 | +10 stop | DOGE | DOWN | 0.46 | 0.64 | 1.45 |
| 11-05 12:55 | +10 stop | ZEC | UP | 0.70 | 0.92 | 1.99 |
| 11-05 12:54 | +10 stop | BNB | DOWN | 0.64 | 0.46 | -2.15 |
| 11-05 12:54 | +5 | BNB | DOWN | 0.64 | open |  |
| 11-05 12:54 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-05 12:54 | +10 stop | XRP | DOWN | 0.58 | 0.76 | 1.49 |
| 11-05 12:54 | +10 stop | ZEC | DOWN | 0.49 | 0.61 | 0.85 |
| 11-05 12:53 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-05 12:53 | +10 stop | ZEC | UP | 0.56 | 0.34 | -2.54 |
| 11-05 12:53 | +5 | ZEC | UP | 0.58 | 0.70 | 0.87 |
| 11-05 12:52 | +10 stop | BNB | DOWN | 0.64 | 0.78 | 1.12 |
| 11-05 12:52 | +5 | BNB | DOWN | 0.64 | 0.78 | 1.12 |
| 11-05 12:52 | +5 | NEAR | DOWN | 0.62 | 0.77 | 1.20 |
| 11-05 12:52 | +10 stop | SOL | UP | 0.60 | 0.34 | -2.93 |
| 11-05 12:52 | +10 stop | DOGE | DOWN | 0.55 | 0.67 | 0.86 |
| 11-05 12:51 | +10 stop | XRP | DOWN | 0.58 | 0.76 | 1.49 |
| 11-05 12:51 | +10 stop | ZEC | DOWN | 0.45 | 0.58 | 0.94 |
| 11-05 12:50 | +5 | BNB | DOWN | 0.66 | 0.72 | 0.29 |
| 11-05 12:50 | +15 | XRP | UP | 0.66 | open |  |
| 11-05 12:50 | +5 | XRP | UP | 0.66 | open |  |
| 11-05 12:50 | +5 | SOL | UP | 0.68 | open |  |
| 11-05 12:49 | +10 stop | XRP | UP | 0.66 | 0.49 | -2.04 |
| 11-05 12:49 | +10 | XRP | UP | 0.66 | open |  |
| 11-05 12:49 | +5 | XRP | UP | 0.66 | 0.73 | 0.40 |
| 11-05 12:49 | +10 stop | SOL | UP | 0.60 | 0.41 | -2.24 |
| 11-05 12:49 | +20 | SOL | UP | 0.60 | open |  |
| 11-05 12:49 | +15 | SOL | UP | 0.60 | open |  |
| 11-05 12:49 | +10 | SOL | UP | 0.60 | 0.71 | 0.78 |
| 11-05 12:49 | +5 | SOL | UP | 0.60 | 0.68 | 0.47 |
| 11-05 12:49 | +10 stop | ETH | UP | 0.58 | 0.38 | -2.35 |
| 11-05 12:49 | +20 | ETH | UP | 0.58 | open |  |
| 11-05 12:49 | +15 | ETH | UP | 0.58 | open |  |
