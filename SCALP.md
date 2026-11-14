# Range-Scalp Bot

*Updated Sat Nov 14 17:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59626 | 52028 | 7598 (107) | 1 | $-16104.43 | -4.3% |
| **+10¢** | 44540 | 35643 | 8897 (143) | 2 | $-15129.80 | -5.4% |
| **+15¢** | 37320 | 27726 | 9594 (180) | 2 | $-13754.24 | -5.9% |
| **+20¢** | 33244 | 23175 | 10069 (232) | 2 | $-12125.83 | -5.8% |
| **+10¢ (15¢ stop)** | 72548 | 72405 | 143 (82) | 0 | $-26687.56 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 17:23 | +5 | HYPE | UP | 0.71 | 0.89 | 1.58 |
| 11-14 17:22 | +10 stop | HYPE | DOWN | 0.45 | 0.09 | -3.83 |
| 11-14 17:22 | +20 | HYPE | DOWN | 0.45 | open |  |
| 11-14 17:22 | +15 | HYPE | DOWN | 0.45 | open |  |
| 11-14 17:22 | +10 | HYPE | DOWN | 0.47 | open |  |
| 11-14 17:22 | +5 | HYPE | DOWN | 0.47 | 0.54 | 0.34 |
| 11-14 17:22 | +10 stop | NEAR | DOWN | 0.48 | 0.25 | -2.62 |
| 11-14 17:22 | +10 stop | ZEC | DOWN | 0.58 | 0.41 | -2.05 |
| 11-14 17:22 | +15 | ZEC | DOWN | 0.58 | open |  |
| 11-14 17:22 | +10 | ZEC | DOWN | 0.58 | open |  |
| 11-14 17:22 | +5 | ZEC | DOWN | 0.56 | 0.64 | 0.45 |
| 11-14 17:22 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 11-14 17:21 | +10 stop | BNB | DOWN | 0.58 | 0.34 | -2.74 |
| 11-14 17:21 | +10 stop | ETH | DOWN | 0.60 | 0.38 | -2.54 |
| 11-14 17:21 | +5 | ETH | DOWN | 0.60 | 0.67 | 0.37 |
| 11-14 17:21 | +10 stop | BTC | DOWN | 0.61 | 0.37 | -2.74 |
| 11-14 17:21 | +5 | BTC | DOWN | 0.61 | open |  |
| 11-14 17:21 | +10 stop | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 11-14 17:21 | +10 | DOGE | UP | 0.52 | 0.62 | 0.65 |
| 11-14 17:21 | +5 | DOGE | UP | 0.54 | 0.62 | 0.45 |
| 11-14 17:21 | +20 | ETH | UP | 0.49 | 0.72 | 1.97 |
| 11-14 17:21 | +10 | ETH | UP | 0.49 | 0.60 | 0.75 |
| 11-14 17:21 | +5 | ETH | UP | 0.49 | 0.54 | 0.14 |
| 11-14 17:20 | +5 | NEAR | UP | 0.58 | 0.73 | 1.18 |
| 11-14 17:19 | +5 | BNB | UP | 0.69 | 0.83 | 1.15 |
| 11-14 17:19 | +10 stop | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-14 17:19 | +15 | HYPE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-14 17:19 | +10 | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-14 17:19 | +5 | HYPE | DOWN | 0.65 | 0.72 | 0.39 |
| 11-14 17:19 | +10 stop | XRP | UP | 0.64 | 0.46 | -2.15 |
| 11-14 17:19 | +10 stop | BNB | UP | 0.71 | 0.52 | -2.23 |
| 11-14 17:19 | +10 stop | SOL | UP | 0.71 | 0.49 | -2.53 |
| 11-14 17:19 | +5 | SOL | UP | 0.71 | 0.77 | 0.32 |
| 11-14 17:18 | +15 | ETH | UP | 0.62 | 0.91 | 2.71 |
| 11-14 17:18 | +10 | ETH | UP | 0.62 | 0.76 | 1.10 |
| 11-14 17:18 | +5 | NEAR | UP | 0.53 | 0.61 | 0.45 |
| 11-14 17:18 | +10 stop | BNB | UP | 0.69 | 0.54 | -1.83 |
| 11-14 17:17 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 11-14 17:17 | +10 stop | ETH | UP | 0.69 | 0.54 | -1.83 |
| 11-14 17:17 | +10 stop | BTC | UP | 0.70 | 0.51 | -2.23 |
