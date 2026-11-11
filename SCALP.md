# Range-Scalp Bot

*Updated Wed Nov 11 14:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55955 | 48791 | 7164 (94) | 3 | $-15340.58 | -4.4% |
| **+10¢** | 41805 | 33450 | 8355 (124) | 3 | $-14285.26 | -5.4% |
| **+15¢** | 35058 | 26046 | 9012 (158) | 2 | $-13043.76 | -5.9% |
| **+20¢** | 31226 | 21772 | 9454 (208) | 3 | $-11418.17 | -5.8% |
| **+10¢ (15¢ stop)** | 68168 | 68047 | 121 (73) | 0 | $-25094.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 14:37 | +10 stop | HYPE | UP | 0.61 | 0.76 | 1.20 |
| 11-11 14:37 | +10 stop | SOL | UP | 0.66 | 0.79 | 1.02 |
| 11-11 14:37 | +10 | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-11 14:37 | +5 | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-11 14:37 | +5 | ETH | DOWN | 0.59 | open |  |
| 11-11 14:36 | +10 stop | XRP | UP | 0.65 | 0.89 | 2.17 |
| 11-11 14:36 | +5 | ETH | DOWN | 0.50 | 0.64 | 1.05 |
| 11-11 14:36 | +10 stop | DOGE | UP | 0.59 | 0.69 | 0.68 |
| 11-11 14:36 | +15 | DOGE | UP | 0.59 | 0.78 | 1.60 |
| 11-11 14:36 | +5 | SOL | UP | 0.58 | 0.67 | 0.56 |
| 11-11 14:36 | +5 | DOGE | UP | 0.61 | 0.66 | 0.17 |
| 11-11 14:36 | +10 stop | HYPE | DOWN | 0.61 | 0.38 | -2.64 |
| 11-11 14:36 | +10 | HYPE | DOWN | 0.61 | open |  |
| 11-11 14:36 | +5 | HYPE | DOWN | 0.61 | open |  |
| 11-11 14:36 | +10 stop | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 11-11 14:35 | +5 | ETH | DOWN | 0.59 | 0.65 | 0.27 |
| 11-11 14:35 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 11-11 14:35 | +10 stop | DOGE | DOWN | 0.53 | 0.33 | -2.34 |
| 11-11 14:35 | +10 | DOGE | DOWN | 0.54 | open |  |
| 11-11 14:35 | +5 | DOGE | DOWN | 0.54 | 0.61 | 0.35 |
| 11-11 14:34 | +10 stop | XRP | DOWN | 0.62 | 0.46 | -1.95 |
| 11-11 14:34 | +5 | XRP | DOWN | 0.65 | open |  |
| 11-11 14:34 | +10 stop | BTC | DOWN | 0.68 | 0.52 | -1.94 |
| 11-11 14:34 | +10 stop | ETH | DOWN | 0.60 | 0.28 | -3.52 |
| 11-11 14:34 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-11 14:34 | +15 | ETH | DOWN | 0.60 | open |  |
| 11-11 14:34 | +10 | ETH | DOWN | 0.60 | open |  |
| 11-11 14:34 | +5 | ETH | DOWN | 0.60 | 0.68 | 0.47 |
| 11-11 14:34 | +10 stop | DOGE | UP | 0.46 | 0.57 | 0.74 |
| 11-11 14:34 | +20 | DOGE | UP | 0.47 | 0.69 | 1.87 |
| 11-11 14:34 | +15 | DOGE | UP | 0.47 | 0.63 | 1.25 |
| 11-11 14:34 | +10 | DOGE | UP | 0.47 | 0.57 | 0.64 |
| 11-11 14:34 | +5 | DOGE | UP | 0.47 | 0.57 | 0.64 |
| 11-11 14:34 | +10 stop | SOL | UP | 0.53 | 0.67 | 1.06 |
| 11-11 14:34 | +20 | SOL | UP | 0.53 | 0.79 | 2.30 |
| 11-11 14:34 | +15 | SOL | UP | 0.53 | 0.79 | 2.30 |
| 11-11 14:34 | +10 | SOL | UP | 0.53 | 0.67 | 1.06 |
| 11-11 14:34 | +5 | SOL | UP | 0.53 | 0.62 | 0.55 |
| 11-11 14:33 | +5 | XRP | UP | 0.60 | 0.67 | 0.37 |
| 11-11 14:33 | +10 stop | BNB | UP | 0.61 | 0.27 | -3.71 |
