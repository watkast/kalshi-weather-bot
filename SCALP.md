# Range-Scalp Bot

*Updated Sat Nov 21 21:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67812 | 59187 | 8625 (138) | 0 | $-18152.47 | -4.3% |
| **+10¢** | 50634 | 40557 | 10077 (181) | 0 | $-16824.65 | -5.3% |
| **+15¢** | 42444 | 31582 | 10862 (230) | 0 | $-15071.22 | -5.7% |
| **+20¢** | 37781 | 26365 | 11416 (288) | 1 | $-13397.39 | -5.7% |
| **+10¢ (15¢ stop)** | 82532 | 82354 | 178 (110) | 0 | $-30280.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 21:31 | +10 stop | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-21 21:31 | +20 | ZEC | DOWN | 0.68 | open |  |
| 11-21 21:31 | +15 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-21 21:31 | +10 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-21 21:31 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-21 21:30 | +10 stop | HYPE | DOWN | 0.59 | 0.70 | 0.78 |
| 11-21 21:30 | +20 | HYPE | DOWN | 0.58 | 0.80 | 1.88 |
| 11-21 21:30 | +15 | HYPE | DOWN | 0.58 | 0.78 | 1.73 |
| 11-21 21:30 | +10 | HYPE | DOWN | 0.58 | 0.70 | 0.91 |
| 11-21 21:30 | +5 | HYPE | DOWN | 0.58 | 0.63 | 0.19 |
| 11-21 21:28 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-21 21:28 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-21 21:28 | +5 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-21 21:27 | +10 stop | XRP | DOWN | 0.61 | 0.85 | 2.14 |
| 11-21 21:26 | +10 stop | ETH | DOWN | 0.61 | 0.43 | -2.15 |
| 11-21 21:26 | +15 | ETH | DOWN | 0.61 | yes | -6.27 |
| 11-21 21:26 | +10 | ETH | DOWN | 0.61 | yes | -6.27 |
| 11-21 21:25 | +10 stop | XRP | DOWN | 0.67 | 0.51 | -1.94 |
| 11-21 21:25 | +10 | XRP | DOWN | 0.67 | 0.85 | 1.55 |
| 11-21 21:25 | +5 | XRP | DOWN | 0.67 | 0.85 | 1.55 |
| 11-21 21:25 | +10 stop | DOGE | DOWN | 0.69 | 0.86 | 1.46 |
| 11-21 21:25 | +10 | DOGE | DOWN | 0.69 | 0.86 | 1.50 |
| 11-21 21:25 | +5 | DOGE | DOWN | 0.69 | 0.76 | 0.46 |
| 11-21 21:25 | +10 stop | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-21 21:23 | +10 stop | XRP | UP | 0.57 | 0.40 | -2.05 |
| 11-21 21:22 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 11-21 21:22 | +10 stop | SOL | DOWN | 0.57 | 0.70 | 0.97 |
| 11-21 21:22 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-21 21:22 | +10 stop | ZEC | UP | 0.65 | 0.34 | -3.42 |
| 11-21 21:22 | +10 stop | XRP | UP | 0.71 | 0.55 | -1.93 |
| 11-21 21:22 | +10 stop | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 11-21 21:21 | +10 stop | DOGE | UP | 0.65 | 0.48 | -2.04 |
| 11-21 21:20 | +10 stop | SOL | UP | 0.66 | 0.46 | -2.34 |
| 11-21 21:20 | +10 stop | ETH | UP | 0.61 | 0.44 | -2.05 |
| 11-21 21:20 | +10 stop | BTC | UP | 0.62 | 0.37 | -2.84 |
| 11-21 21:20 | +5 | ETH | UP | 0.59 | 0.73 | 1.09 |
| 11-21 21:20 | +10 stop | BNB | UP | 0.66 | 0.49 | -2.04 |
| 11-21 21:20 | +5 | BNB | UP | 0.66 | no | -6.76 |
| 11-21 21:20 | +10 stop | NEAR | DOWN | 0.61 | 0.72 | 0.78 |
| 11-21 21:20 | +20 | NEAR | DOWN | 0.61 | 0.82 | 1.82 |
