# Range-Scalp Bot

*Updated Sat Oct 17 18:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21413 | 18656 | 2757 (29) | 2 | $-6132.27 | -4.5% |
| **+10¢** | 16099 | 12911 | 3188 (41) | 2 | $-5474.28 | -5.4% |
| **+15¢** | 13461 | 10025 | 3436 (61) | 2 | $-4961.81 | -5.9% |
| **+20¢** | 11926 | 8325 | 3601 (80) | 2 | $-4410.26 | -5.9% |
| **+10¢ (15¢ stop)** | 26280 | 26230 | 50 (29) | 2 | $-10002.10 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 18:45 | +10 stop | NEAR | UP | 0.63 | open |  |
| 10-17 18:45 | +20 | NEAR | UP | 0.63 | open |  |
| 10-17 18:45 | +15 | NEAR | UP | 0.63 | open |  |
| 10-17 18:45 | +10 | NEAR | UP | 0.63 | open |  |
| 10-17 18:45 | +5 | NEAR | UP | 0.63 | open |  |
| 10-17 18:45 | +10 stop | ETH | UP | 0.61 | open |  |
| 10-17 18:45 | +20 | ETH | UP | 0.61 | open |  |
| 10-17 18:45 | +15 | ETH | UP | 0.61 | open |  |
| 10-17 18:45 | +10 | ETH | UP | 0.61 | open |  |
| 10-17 18:45 | +5 | ETH | UP | 0.61 | open |  |
| 10-17 18:43 | +10 stop | HYPE | DOWN | 0.35 | 0.50 | 1.16 |
| 10-17 18:43 | +15 | HYPE | DOWN | 0.35 | 0.50 | 1.16 |
| 10-17 18:43 | +10 | HYPE | DOWN | 0.35 | 0.50 | 1.17 |
| 10-17 18:43 | +5 | HYPE | DOWN | 0.33 | 0.50 | 1.36 |
| 10-17 18:43 | +10 stop | BNB | UP | 0.59 | 0.81 | 1.92 |
| 10-17 18:42 | +10 stop | XRP | UP | 0.67 | 0.93 | 2.36 |
| 10-17 18:41 | +10 stop | BNB | UP | 0.63 | 0.47 | -1.95 |
| 10-17 18:41 | +5 | BNB | UP | 0.63 | 0.81 | 1.52 |
| 10-17 18:40 | +10 stop | BTC | DOWN | 0.57 | 0.21 | -3.90 |
| 10-17 18:39 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-17 18:39 | +20 | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-17 18:39 | +15 | HYPE | DOWN | 0.61 | 0.78 | 1.40 |
| 10-17 18:39 | +10 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-17 18:39 | +5 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-17 18:37 | +10 stop | XRP | UP | 0.59 | 0.69 | 0.68 |
| 10-17 18:37 | +10 stop | BNB | UP | 0.66 | 0.42 | -2.74 |
| 10-17 18:37 | +10 stop | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 10-17 18:37 | +5 | DOGE | UP | 0.67 | 0.74 | 0.40 |
| 10-17 18:36 | +10 stop | BTC | UP | 0.59 | 0.70 | 0.78 |
| 10-17 18:36 | +10 stop | ETH | DOWN | 0.68 | 0.91 | 2.02 |
| 10-17 18:36 | +5 | ETH | DOWN | 0.68 | 0.91 | 2.02 |
| 10-17 18:35 | +10 stop | ZEC | UP | 0.66 | 0.80 | 1.12 |
| 10-17 18:35 | +10 stop | SOL | UP | 0.57 | 0.67 | 0.66 |
| 10-17 18:34 | +10 stop | XRP | DOWN | 0.61 | 0.45 | -1.95 |
| 10-17 18:34 | +10 | XRP | DOWN | 0.61 | yes | -6.27 |
| 10-17 18:34 | +5 | BNB | DOWN | 0.60 | 0.65 | 0.17 |
| 10-17 18:34 | +5 | XRP | DOWN | 0.63 | yes | -6.47 |
| 10-17 18:34 | +10 stop | DOGE | DOWN | 0.57 | 0.37 | -2.35 |
| 10-17 18:34 | +10 stop | BNB | DOWN | 0.59 | 0.41 | -2.15 |
| 10-17 18:34 | +10 stop | SOL | DOWN | 0.48 | 0.58 | 0.64 |
