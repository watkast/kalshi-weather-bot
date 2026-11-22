# Range-Scalp Bot

*Updated Sun Nov 22 22:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69186 | 60367 | 8819 (145) | 4 | $-18639.41 | -4.3% |
| **+10¢** | 51629 | 41333 | 10296 (188) | 5 | $-17286.78 | -5.3% |
| **+15¢** | 43269 | 32171 | 11098 (241) | 6 | $-15496.96 | -5.7% |
| **+20¢** | 38534 | 26871 | 11663 (300) | 6 | $-13782.71 | -5.7% |
| **+10¢ (15¢ stop)** | 84271 | 84082 | 189 (117) | 2 | $-31047.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 22:41 | +10 stop | ETH | UP | 0.71 | open |  |
| 11-22 22:41 | +10 stop | ETH | UP | 0.58 | 0.68 | 0.66 |
| 11-22 22:40 | +10 stop | SOL | UP | 0.48 | 0.59 | 0.75 |
| 11-22 22:40 | +10 | SOL | UP | 0.48 | 0.59 | 0.75 |
| 11-22 22:40 | +5 | SOL | UP | 0.48 | 0.59 | 0.75 |
| 11-22 22:40 | +10 stop | BNB | UP | 0.58 | 0.74 | 1.28 |
| 11-22 22:40 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 11-22 22:40 | +5 | XRP | DOWN | 0.68 | 0.74 | 0.33 |
| 11-22 22:40 | +10 stop | HYPE | UP | 0.67 | 0.50 | -2.04 |
| 11-22 22:40 | +10 stop | XRP | UP | 0.47 | 0.64 | 1.35 |
| 11-22 22:40 | +5 | XRP | UP | 0.46 | 0.64 | 1.45 |
| 11-22 22:38 | +10 stop | ZEC | UP | 0.57 | 0.77 | 1.69 |
| 11-22 22:38 | +10 stop | HYPE | UP | 0.58 | 0.68 | 0.66 |
| 11-22 22:37 | +10 stop | XRP | DOWN | 0.49 | 0.32 | -2.04 |
| 11-22 22:37 | +10 stop | XRP | DOWN | 0.53 | 0.66 | 0.96 |
| 11-22 22:37 | +10 stop | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-22 22:37 | +15 | BTC | UP | 0.67 | 0.82 | 1.23 |
| 11-22 22:37 | +10 | BTC | UP | 0.67 | 0.79 | 0.92 |
| 11-22 22:37 | +5 | BTC | UP | 0.67 | 0.76 | 0.61 |
| 11-22 22:37 | +10 stop | SOL | UP | 0.51 | 0.64 | 0.95 |
| 11-22 22:37 | +10 | SOL | UP | 0.51 | 0.64 | 0.95 |
| 11-22 22:37 | +5 | SOL | UP | 0.51 | 0.64 | 0.95 |
| 11-22 22:37 | +10 stop | ETH | UP | 0.56 | 0.76 | 1.69 |
| 11-22 22:36 | +10 stop | XRP | DOWN | 0.56 | 0.66 | 0.66 |
| 11-22 22:36 | +10 stop | BTC | UP | 0.56 | 0.73 | 1.38 |
| 11-22 22:36 | +20 | BTC | UP | 0.56 | 0.76 | 1.69 |
| 11-22 22:36 | +15 | BTC | UP | 0.56 | 0.73 | 1.38 |
| 11-22 22:36 | +10 | BTC | UP | 0.56 | 0.73 | 1.38 |
| 11-22 22:36 | +5 | BTC | UP | 0.56 | 0.73 | 1.38 |
| 11-22 22:35 | +5 | ZEC | DOWN | 0.64 | open |  |
| 11-22 22:35 | +10 stop | HYPE | DOWN | 0.63 | 0.39 | -2.72 |
| 11-22 22:35 | +10 stop | ZEC | DOWN | 0.63 | 0.31 | -3.52 |
| 11-22 22:35 | +10 stop | BNB | UP | 0.70 | 0.80 | 0.73 |
| 11-22 22:35 | +10 stop | ETH | UP | 0.69 | 0.54 | -1.83 |
| 11-22 22:34 | +15 | ZEC | DOWN | 0.57 | open |  |
| 11-22 22:34 | +5 | ZEC | DOWN | 0.57 | 0.63 | 0.26 |
| 11-22 22:33 | +10 stop | BNB | UP | 0.67 | 0.77 | 0.71 |
| 11-22 22:33 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-22 22:33 | +10 stop | SOL | UP | 0.70 | 0.80 | 0.73 |
| 11-22 22:33 | +20 | SOL | UP | 0.70 | open |  |
