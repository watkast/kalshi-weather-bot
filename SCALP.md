# Range-Scalp Bot

*Updated Wed Oct 07 19:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 6726 | 5836 | 890 (10) | 3 | $-2061.88 | -4.9% |
| **+10¢** | 5109 | 4067 | 1042 (17) | 3 | $-1932.81 | -6.0% |
| **+15¢** | 4282 | 3184 | 1098 (21) | 2 | $-1618.75 | -6.0% |
| **+20¢** | 3827 | 2683 | 1144 (28) | 2 | $-1292.00 | -5.4% |
| **+10¢ (15¢ stop)** | 8181 | 8164 | 17 (10) | 0 | $-2928.34 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 19:38 | +10 stop | ETH | DOWN | 0.50 | 0.63 | 0.95 |
| 10-07 19:37 | +10 stop | ETH | DOWN | 0.46 | 0.60 | 1.05 |
| 10-07 19:36 | +10 stop | ETH | DOWN | 0.71 | 0.54 | -2.03 |
| 10-07 19:36 | +10 | ETH | DOWN | 0.71 | open |  |
| 10-07 19:36 | +5 | ETH | DOWN | 0.71 | open |  |
| 10-07 19:36 | +10 stop | ETH | UP | 0.43 | 0.65 | 1.86 |
| 10-07 19:36 | +10 | ETH | UP | 0.46 | 0.65 | 1.56 |
| 10-07 19:36 | +5 | ETH | UP | 0.46 | 0.65 | 1.56 |
| 10-07 19:35 | +5 | XRP | UP | 0.59 | open |  |
| 10-07 19:35 | +10 stop | HYPE | UP | 0.58 | 0.38 | -2.35 |
| 10-07 19:34 | +10 stop | XRP | UP | 0.62 | 0.45 | -2.01 |
| 10-07 19:34 | +10 stop | BTC | UP | 0.57 | 0.24 | -3.61 |
| 10-07 19:34 | +5 | BTC | UP | 0.57 | open |  |
| 10-07 19:34 | +10 stop | SOL | UP | 0.59 | 0.43 | -1.95 |
| 10-07 19:33 | +5 | BNB | DOWN | 0.60 | 0.67 | 0.37 |
| 10-07 19:33 | +10 stop | DOGE | DOWN | 0.54 | 0.39 | -1.85 |
| 10-07 19:33 | +20 | DOGE | DOWN | 0.54 | 0.82 | 2.51 |
| 10-07 19:33 | +15 | DOGE | DOWN | 0.54 | 0.82 | 2.51 |
| 10-07 19:33 | +10 | DOGE | DOWN | 0.54 | 0.82 | 2.51 |
| 10-07 19:33 | +5 | DOGE | DOWN | 0.54 | 0.82 | 2.51 |
| 10-07 19:33 | +10 stop | XRP | DOWN | 0.61 | 0.36 | -2.84 |
| 10-07 19:32 | +5 | SOL | DOWN | 0.64 | 0.69 | 0.18 |
| 10-07 19:32 | +10 stop | ZEC | DOWN | 0.51 | 0.28 | -2.63 |
| 10-07 19:31 | +10 stop | BTC | UP | 0.57 | 0.40 | -2.05 |
| 10-07 19:31 | +20 | BTC | UP | 0.57 | open |  |
| 10-07 19:31 | +15 | BTC | UP | 0.57 | open |  |
| 10-07 19:31 | +10 | BTC | UP | 0.57 | open |  |
| 10-07 19:31 | +5 | BTC | UP | 0.57 | 0.62 | 0.15 |
| 10-07 19:31 | +10 stop | XRP | UP | 0.59 | 0.42 | -2.05 |
| 10-07 19:31 | +20 | XRP | UP | 0.59 | open |  |
| 10-07 19:31 | +15 | XRP | UP | 0.59 | open |  |
| 10-07 19:31 | +10 | XRP | UP | 0.59 | open |  |
| 10-07 19:31 | +5 | XRP | UP | 0.59 | 0.65 | 0.27 |
| 10-07 19:31 | +10 stop | SOL | DOWN | 0.57 | 0.42 | -1.86 |
| 10-07 19:31 | +20 | SOL | DOWN | 0.57 | 0.84 | 2.42 |
| 10-07 19:31 | +15 | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 10-07 19:31 | +10 | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 10-07 19:31 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 10-07 19:31 | +10 stop | ZEC | UP | 0.61 | 0.45 | -1.95 |
| 10-07 19:31 | +20 | ZEC | UP | 0.62 | 0.85 | 2.05 |
