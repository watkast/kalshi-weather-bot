# Range-Scalp Bot

*Updated Wed Nov 11 12:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55843 | 48698 | 7145 (94) | 3 | $-15266.37 | -4.3% |
| **+10¢** | 41726 | 33395 | 8331 (124) | 3 | $-14189.54 | -5.4% |
| **+15¢** | 34988 | 26000 | 8988 (158) | 3 | $-12958.24 | -5.9% |
| **+20¢** | 31161 | 21733 | 9428 (208) | 4 | $-11329.90 | -5.8% |
| **+10¢ (15¢ stop)** | 68027 | 67906 | 121 (73) | 0 | $-25019.49 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 12:56 | +10 stop | ETH | UP | 0.40 | 0.57 | 1.35 |
| 11-11 12:56 | +20 | ETH | UP | 0.40 | open |  |
| 11-11 12:56 | +15 | ETH | UP | 0.40 | 0.57 | 1.35 |
| 11-11 12:56 | +10 | ETH | UP | 0.40 | 0.57 | 1.35 |
| 11-11 12:56 | +5 | ETH | UP | 0.41 | 0.57 | 1.25 |
| 11-11 12:56 | +10 stop | NEAR | DOWN | 0.62 | 0.78 | 1.30 |
| 11-11 12:56 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-11 12:54 | +10 stop | NEAR | DOWN | 0.51 | 0.62 | 0.76 |
| 11-11 12:54 | +10 stop | ZEC | DOWN | 0.65 | 0.46 | -2.24 |
| 11-11 12:53 | +10 stop | BTC | UP | 0.61 | 0.46 | -1.85 |
| 11-11 12:53 | +20 | BTC | UP | 0.61 | open |  |
| 11-11 12:53 | +15 | BTC | UP | 0.61 | open |  |
| 11-11 12:53 | +10 | BTC | UP | 0.61 | open |  |
| 11-11 12:53 | +5 | BTC | UP | 0.61 | open |  |
| 11-11 12:51 | +10 stop | NEAR | UP | 0.63 | 0.44 | -2.22 |
| 11-11 12:51 | +10 stop | ZEC | UP | 0.57 | 0.34 | -2.62 |
| 11-11 12:51 | +15 | ZEC | UP | 0.56 | open |  |
| 11-11 12:51 | +10 | ZEC | UP | 0.56 | open |  |
| 11-11 12:51 | +5 | ZEC | UP | 0.56 | open |  |
| 11-11 12:51 | +10 stop | BTC | UP | 0.63 | 0.77 | 1.10 |
| 11-11 12:51 | +20 | BTC | UP | 0.62 | 0.82 | 1.72 |
| 11-11 12:51 | +15 | BTC | UP | 0.62 | 0.77 | 1.20 |
| 11-11 12:51 | +10 | BTC | UP | 0.62 | 0.77 | 1.20 |
| 11-11 12:51 | +5 | BTC | UP | 0.62 | 0.69 | 0.38 |
| 11-11 12:50 | +10 stop | NEAR | UP | 0.64 | 0.48 | -1.95 |
| 11-11 12:50 | +15 | NEAR | UP | 0.64 | open |  |
| 11-11 12:50 | +10 | NEAR | UP | 0.65 | open |  |
| 11-11 12:50 | +5 | NEAR | UP | 0.65 | open |  |
| 11-11 12:47 | +5 | NEAR | UP | 0.65 | 0.70 | 0.20 |
| 11-11 12:46 | +10 stop | ZEC | UP | 0.65 | 0.83 | 1.54 |
| 11-11 12:46 | +20 | ZEC | UP | 0.65 | open |  |
| 11-11 12:46 | +15 | ZEC | UP | 0.65 | 0.83 | 1.54 |
| 11-11 12:46 | +10 | ZEC | UP | 0.65 | 0.83 | 1.54 |
| 11-11 12:46 | +5 | ZEC | UP | 0.65 | 0.72 | 0.39 |
| 11-11 12:45 | +10 stop | ETH | UP | 0.70 | 0.83 | 1.05 |
| 11-11 12:45 | +20 | ETH | UP | 0.70 | 0.92 | 1.95 |
| 11-11 12:45 | +15 | ETH | UP | 0.70 | 0.85 | 1.26 |
| 11-11 12:45 | +10 | ETH | UP | 0.70 | 0.83 | 1.05 |
| 11-11 12:45 | +5 | ETH | UP | 0.70 | 0.76 | 0.32 |
| 11-11 12:45 | +10 stop | BTC | UP | 0.65 | 0.76 | 0.81 |
