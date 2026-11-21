# Range-Scalp Bot

*Updated Sat Nov 21 15:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67506 | 58915 | 8591 (134) | 5 | $-18113.78 | -4.3% |
| **+10¢** | 50417 | 40383 | 10034 (175) | 6 | $-16786.92 | -5.3% |
| **+15¢** | 42275 | 31459 | 10816 (225) | 6 | $-15030.70 | -5.7% |
| **+20¢** | 37626 | 26260 | 11366 (283) | 6 | $-13351.21 | -5.7% |
| **+10¢ (15¢ stop)** | 82173 | 82002 | 171 (105) | 3 | $-30160.65 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 15:06 | +10 stop | BTC | UP | 0.65 | open |  |
| 11-21 15:06 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 11-21 15:06 | +10 | NEAR | DOWN | 0.69 | open |  |
| 11-21 15:06 | +5 | NEAR | DOWN | 0.69 | open |  |
| 11-21 15:06 | +10 stop | ZEC | UP | 0.50 | open |  |
| 11-21 15:05 | +10 | NEAR | DOWN | 0.50 | 0.64 | 1.05 |
| 11-21 15:05 | +5 | NEAR | DOWN | 0.50 | 0.64 | 1.05 |
| 11-21 15:05 | +10 stop | XRP | UP | 0.70 | 0.85 | 1.26 |
| 11-21 15:05 | +10 stop | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 11-21 15:05 | +10 | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 11-21 15:05 | +5 | HYPE | UP | 0.68 | 0.73 | 0.20 |
| 11-21 15:04 | +5 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-21 15:04 | +10 stop | ZEC | DOWN | 0.63 | 0.41 | -2.54 |
| 11-21 15:04 | +15 | ZEC | DOWN | 0.63 | open |  |
| 11-21 15:04 | +10 | ZEC | DOWN | 0.63 | open |  |
| 11-21 15:04 | +5 | BNB | DOWN | 0.59 | open |  |
| 11-21 15:03 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.38 |
| 11-21 15:03 | +5 | ZEC | DOWN | 0.66 | open |  |
| 11-21 15:02 | +10 stop | SOL | UP | 0.66 | 0.80 | 1.12 |
| 11-21 15:02 | +10 | SOL | UP | 0.66 | 0.80 | 1.12 |
| 11-21 15:02 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 11-21 15:02 | +10 stop | HYPE | UP | 0.57 | 0.68 | 0.76 |
| 11-21 15:02 | +20 | HYPE | UP | 0.57 | 0.79 | 1.90 |
| 11-21 15:02 | +15 | HYPE | UP | 0.57 | 0.73 | 1.28 |
| 11-21 15:02 | +10 | HYPE | UP | 0.57 | 0.68 | 0.76 |
| 11-21 15:02 | +5 | HYPE | UP | 0.57 | 0.68 | 0.76 |
| 11-21 15:02 | +10 stop | DOGE | UP | 0.61 | 0.73 | 0.89 |
| 11-21 15:02 | +20 | DOGE | UP | 0.61 | 0.86 | 2.24 |
| 11-21 15:02 | +15 | DOGE | UP | 0.61 | 0.77 | 1.30 |
| 11-21 15:02 | +10 | DOGE | UP | 0.61 | 0.73 | 0.89 |
| 11-21 15:02 | +5 | DOGE | UP | 0.61 | 0.66 | 0.17 |
| 11-21 15:02 | +10 stop | ETH | DOWN | 0.52 | 0.23 | -3.21 |
| 11-21 15:02 | +20 | ETH | DOWN | 0.52 | open |  |
| 11-21 15:02 | +15 | ETH | DOWN | 0.52 | open |  |
| 11-21 15:02 | +10 | ETH | DOWN | 0.52 | open |  |
| 11-21 15:02 | +5 | ETH | DOWN | 0.52 | 0.57 | 0.14 |
| 11-21 15:01 | +10 stop | BTC | DOWN | 0.53 | 0.37 | -1.95 |
| 11-21 15:01 | +20 | BTC | DOWN | 0.53 | open |  |
| 11-21 15:01 | +15 | BTC | DOWN | 0.53 | open |  |
| 11-21 15:01 | +10 | BTC | DOWN | 0.53 | open |  |
