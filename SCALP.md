# Range-Scalp Bot

*Updated Wed Oct 07 14:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6591 | 5731 | 860 (9) | 7 | $-1936.35 | -4.7% |
| **+10¢** | 5004 | 3993 | 1011 (16) | 5 | $-1819.71 | -5.8% |
| **+15¢** | 4188 | 3121 | 1067 (20) | 6 | $-1528.02 | -5.8% |
| **+20¢** | 3742 | 2628 | 1114 (27) | 7 | $-1221.52 | -5.2% |
| **+10¢ (15¢ stop)** | 8001 | 7986 | 15 (9) | 6 | $-2836.07 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 14:39 | +10 | BNB | DOWN | 0.70 | open |  |
| 10-07 14:39 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 10-07 14:39 | +10 stop | ETH | DOWN | 0.68 | open |  |
| 10-07 14:38 | +10 stop | DOGE | DOWN | 0.66 | open |  |
| 10-07 14:38 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 10-07 14:38 | +10 stop | SOL | UP | 0.61 | open |  |
| 10-07 14:38 | +5 | SOL | UP | 0.61 | open |  |
| 10-07 14:38 | +10 stop | XRP | DOWN | 0.65 | open |  |
| 10-07 14:38 | +5 | BTC | UP | 0.55 | open |  |
| 10-07 14:37 | +10 stop | BTC | UP | 0.57 | 0.38 | -2.25 |
| 10-07 14:37 | +20 | BTC | UP | 0.57 | open |  |
| 10-07 14:37 | +10 | BTC | UP | 0.57 | open |  |
| 10-07 14:37 | +5 | BTC | UP | 0.57 | 0.63 | 0.25 |
| 10-07 14:37 | +10 stop | BNB | UP | 0.60 | 0.42 | -2.15 |
| 10-07 14:37 | +10 stop | ETH | UP | 0.63 | 0.48 | -1.85 |
| 10-07 14:37 | +20 | ETH | UP | 0.63 | open |  |
| 10-07 14:37 | +10 stop | DOGE | UP | 0.64 | 0.47 | -2.05 |
| 10-07 14:37 | +10 | DOGE | UP | 0.64 | open |  |
| 10-07 14:37 | +5 | DOGE | UP | 0.64 | open |  |
| 10-07 14:37 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 10-07 14:37 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 10-07 14:37 | +10 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 10-07 14:36 | +10 stop | XRP | UP | 0.65 | 0.45 | -2.34 |
| 10-07 14:36 | +10 | ZEC | DOWN | 0.58 | 0.70 | 0.87 |
| 10-07 14:36 | +5 | ZEC | DOWN | 0.56 | 0.62 | 0.25 |
| 10-07 14:35 | +10 stop | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-07 14:35 | +10 | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 10-07 14:35 | +5 | DOGE | UP | 0.64 | 0.72 | 0.48 |
| 10-07 14:35 | +10 stop | ZEC | DOWN | 0.67 | 0.81 | 1.13 |
| 10-07 14:35 | +5 | SOL | UP | 0.60 | 0.68 | 0.47 |
| 10-07 14:35 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 10-07 14:35 | +15 | BTC | UP | 0.67 | open |  |
| 10-07 14:35 | +10 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 10-07 14:35 | +5 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 10-07 14:35 | +10 stop | XRP | DOWN | 0.61 | 0.41 | -2.34 |
| 10-07 14:34 | +15 | ETH | UP | 0.65 | open |  |
| 10-07 14:34 | +10 | ETH | UP | 0.67 | open |  |
| 10-07 14:34 | +5 | NEAR | UP | 0.57 | open |  |
| 10-07 14:34 | +10 stop | SOL | UP | 0.64 | 0.77 | 1.00 |
| 10-07 14:34 | +5 | SOL | UP | 0.64 | 0.72 | 0.48 |
