# Range-Scalp Bot

*Updated Wed Oct 28 20:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38506 | 33606 | 4900 (48) | 8 | $-10786.36 | -4.4% |
| **+10¢** | 28720 | 23061 | 5659 (70) | 9 | $-9552.52 | -5.3% |
| **+15¢** | 24025 | 17948 | 6077 (95) | 9 | $-8489.49 | -5.6% |
| **+20¢** | 21312 | 14949 | 6363 (120) | 9 | $-7416.05 | -5.5% |
| **+10¢ (15¢ stop)** | 47111 | 47044 | 67 (35) | 0 | $-17870.90 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 20:52 | +5 | XRP | UP | 0.61 | 0.71 | 0.71 |
| 10-28 20:52 | +10 stop | BNB | UP | 0.64 | 0.83 | 1.63 |
| 10-28 20:52 | +10 stop | SOL | UP | 0.70 | 0.82 | 0.94 |
| 10-28 20:52 | +10 stop | DOGE | UP | 0.61 | 0.73 | 0.91 |
| 10-28 20:51 | +10 stop | BTC | UP | 0.70 | 0.85 | 1.26 |
| 10-28 20:51 | +10 stop | HYPE | UP | 0.67 | 0.78 | 0.77 |
| 10-28 20:51 | +10 stop | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 10-28 20:51 | +10 stop | XRP | DOWN | 0.56 | 0.34 | -2.54 |
| 10-28 20:51 | +10 | XRP | DOWN | 0.56 | open |  |
| 10-28 20:51 | +5 | XRP | DOWN | 0.56 | 0.62 | 0.25 |
| 10-28 20:50 | +10 stop | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-28 20:50 | +10 | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-28 20:50 | +5 | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 10-28 20:50 | +10 stop | ETH | UP | 0.55 | 0.66 | 0.76 |
| 10-28 20:50 | +5 | BTC | DOWN | 0.60 | open |  |
| 10-28 20:49 | +5 | BTC | DOWN | 0.58 | 0.64 | 0.25 |
| 10-28 20:49 | +10 stop | HYPE | DOWN | 0.58 | 0.43 | -1.86 |
| 10-28 20:49 | +10 stop | NEAR | UP | 0.57 | 0.67 | 0.68 |
| 10-28 20:48 | +10 stop | ZEC | UP | 0.54 | 0.66 | 0.86 |
| 10-28 20:48 | +5 | XRP | DOWN | 0.59 | 0.70 | 0.78 |
| 10-28 20:48 | +5 | BTC | DOWN | 0.59 | 0.66 | 0.37 |
| 10-28 20:47 | +10 stop | BTC | DOWN | 0.59 | 0.44 | -1.85 |
| 10-28 20:47 | +20 | BTC | DOWN | 0.59 | open |  |
| 10-28 20:47 | +15 | BTC | DOWN | 0.61 | open |  |
| 10-28 20:47 | +10 | BTC | DOWN | 0.61 | open |  |
| 10-28 20:47 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-28 20:47 | +10 stop | SOL | DOWN | 0.63 | 0.44 | -2.25 |
| 10-28 20:47 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-28 20:47 | +15 | SOL | DOWN | 0.63 | open |  |
| 10-28 20:47 | +10 | SOL | DOWN | 0.63 | open |  |
| 10-28 20:47 | +5 | SOL | DOWN | 0.63 | open |  |
| 10-28 20:47 | +10 stop | DOGE | DOWN | 0.65 | 0.50 | -1.84 |
| 10-28 20:47 | +20 | DOGE | DOWN | 0.65 | open |  |
| 10-28 20:47 | +15 | DOGE | DOWN | 0.65 | open |  |
| 10-28 20:47 | +10 | DOGE | DOWN | 0.65 | open |  |
| 10-28 20:47 | +5 | DOGE | DOWN | 0.65 | open |  |
| 10-28 20:47 | +10 stop | HYPE | DOWN | 0.70 | 0.47 | -2.63 |
| 10-28 20:47 | +20 | HYPE | DOWN | 0.70 | open |  |
| 10-28 20:47 | +15 | HYPE | DOWN | 0.70 | open |  |
| 10-28 20:47 | +10 | HYPE | DOWN | 0.70 | open |  |
