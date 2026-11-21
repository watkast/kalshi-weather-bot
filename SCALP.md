# Range-Scalp Bot

*Updated Sat Nov 21 23:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67899 | 59268 | 8631 (138) | 8 | $-18127.31 | -4.2% |
| **+10¢** | 50698 | 40611 | 10087 (181) | 7 | $-16822.47 | -5.3% |
| **+15¢** | 42501 | 31626 | 10875 (230) | 7 | $-15081.68 | -5.7% |
| **+20¢** | 37830 | 26399 | 11431 (288) | 8 | $-13418.79 | -5.7% |
| **+10¢ (15¢ stop)** | 82661 | 82483 | 178 (110) | 5 | $-30346.06 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 23:06 | +5 | DOGE | UP | 0.68 | open |  |
| 11-21 23:06 | +10 stop | DOGE | UP | 0.68 | open |  |
| 11-21 23:06 | +5 | SOL | UP | 0.69 | open |  |
| 11-21 23:06 | +10 stop | ETH | UP | 0.65 | open |  |
| 11-21 23:05 | +10 stop | SOL | UP | 0.71 | open |  |
| 11-21 23:05 | +10 stop | NEAR | UP | 0.71 | open |  |
| 11-21 23:05 | +10 stop | HYPE | DOWN | 0.66 | open |  |
| 11-21 23:05 | +15 | HYPE | DOWN | 0.66 | open |  |
| 11-21 23:05 | +10 | HYPE | DOWN | 0.66 | open |  |
| 11-21 23:05 | +5 | HYPE | DOWN | 0.66 | open |  |
| 11-21 23:04 | +10 stop | XRP | UP | 0.67 | 0.77 | 0.71 |
| 11-21 23:04 | +10 stop | BTC | DOWN | 0.65 | 0.49 | -1.94 |
| 11-21 23:04 | +10 | BTC | DOWN | 0.65 | open |  |
| 11-21 23:04 | +5 | BTC | DOWN | 0.65 | open |  |
| 11-21 23:04 | +10 stop | DOGE | DOWN | 0.68 | 0.48 | -2.34 |
| 11-21 23:04 | +10 stop | ETH | DOWN | 0.60 | 0.42 | -2.15 |
| 11-21 23:04 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-21 23:04 | +15 | ETH | DOWN | 0.60 | open |  |
| 11-21 23:04 | +10 | ETH | DOWN | 0.60 | open |  |
| 11-21 23:04 | +5 | ETH | DOWN | 0.60 | open |  |
| 11-21 23:04 | +10 stop | BNB | DOWN | 0.62 | 0.45 | -2.03 |
| 11-21 23:04 | +10 stop | NEAR | DOWN | 0.63 | 0.46 | -2.04 |
| 11-21 23:03 | +10 stop | SOL | DOWN | 0.52 | 0.36 | -1.95 |
| 11-21 23:03 | +10 stop | ZEC | UP | 0.71 | 0.83 | 0.95 |
| 11-21 23:03 | +10 stop | ZEC | DOWN | 0.44 | 0.63 | 1.55 |
| 11-21 23:02 | +5 | XRP | DOWN | 0.69 | open |  |
| 11-21 23:02 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-21 23:02 | +20 | BTC | DOWN | 0.71 | open |  |
| 11-21 23:02 | +15 | BTC | DOWN | 0.71 | open |  |
| 11-21 23:02 | +10 | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-21 23:02 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-21 23:01 | +10 stop | XRP | UP | 0.50 | 0.28 | -2.53 |
| 11-21 23:01 | +20 | XRP | UP | 0.50 | 0.71 | 1.77 |
| 11-21 23:01 | +15 | XRP | UP | 0.50 | 0.71 | 1.77 |
| 11-21 23:01 | +10 | XRP | UP | 0.50 | 0.63 | 0.95 |
| 11-21 23:01 | +5 | XRP | UP | 0.50 | 0.57 | 0.34 |
| 11-21 23:01 | +10 stop | HYPE | DOWN | 0.68 | 0.86 | 1.55 |
| 11-21 23:01 | +20 | HYPE | DOWN | 0.68 | open |  |
| 11-21 23:01 | +15 | HYPE | DOWN | 0.68 | 0.86 | 1.55 |
| 11-21 23:01 | +10 | HYPE | DOWN | 0.68 | 0.86 | 1.55 |
