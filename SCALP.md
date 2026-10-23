# Range-Scalp Bot

*Updated Fri Oct 23 20:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30941 | 26968 | 3973 (39) | 1 | $-8912.47 | -4.6% |
| **+10¢** | 23143 | 18550 | 4593 (57) | 2 | $-7926.97 | -5.4% |
| **+15¢** | 19363 | 14420 | 4943 (80) | 3 | $-7152.86 | -5.9% |
| **+20¢** | 17150 | 11974 | 5176 (103) | 3 | $-6386.21 | -5.9% |
| **+10¢ (15¢ stop)** | 37970 | 37911 | 59 (32) | 1 | $-14501.25 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 20:52 | +10 stop | BNB | DOWN | 0.68 | open |  |
| 10-23 20:51 | +10 stop | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-23 20:51 | +20 | ZEC | UP | 0.70 | open |  |
| 10-23 20:51 | +15 | ZEC | UP | 0.70 | open |  |
| 10-23 20:51 | +10 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-23 20:51 | +5 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-23 20:50 | +10 stop | BNB | UP | 0.65 | 0.49 | -1.94 |
| 10-23 20:50 | +15 | BNB | UP | 0.65 | open |  |
| 10-23 20:50 | +10 | BNB | UP | 0.65 | open |  |
| 10-23 20:50 | +5 | BNB | UP | 0.65 | open |  |
| 10-23 20:48 | +10 stop | BTC | UP | 0.50 | 0.33 | -2.04 |
| 10-23 20:46 | +10 stop | BTC | DOWN | 0.58 | 0.43 | -1.86 |
| 10-23 20:46 | +20 | BTC | DOWN | 0.58 | open |  |
| 10-23 20:46 | +15 | BTC | DOWN | 0.58 | open |  |
| 10-23 20:46 | +10 | BTC | DOWN | 0.58 | open |  |
| 10-23 20:46 | +5 | BTC | DOWN | 0.58 | 0.66 | 0.46 |
| 10-23 20:46 | +10 stop | HYPE | UP | 0.64 | 0.81 | 1.47 |
| 10-23 20:46 | +20 | HYPE | UP | 0.64 | 0.90 | 2.45 |
| 10-23 20:46 | +15 | HYPE | UP | 0.64 | 0.81 | 1.47 |
| 10-23 20:46 | +10 | HYPE | UP | 0.64 | 0.81 | 1.47 |
| 10-23 20:46 | +5 | HYPE | UP | 0.64 | 0.81 | 1.47 |
| 10-23 20:46 | +10 stop | BNB | UP | 0.68 | 0.81 | 1.03 |
| 10-23 20:46 | +20 | BNB | UP | 0.68 | open |  |
| 10-23 20:46 | +15 | BNB | UP | 0.68 | 0.84 | 1.34 |
| 10-23 20:46 | +10 | BNB | UP | 0.68 | 0.81 | 1.03 |
| 10-23 20:46 | +5 | BNB | UP | 0.68 | 0.73 | 0.20 |
| 10-23 20:46 | +10 stop | ETH | UP | 0.64 | 0.74 | 0.69 |
| 10-23 20:46 | +20 | ETH | UP | 0.64 | 0.84 | 1.73 |
| 10-23 20:46 | +15 | ETH | UP | 0.64 | 0.79 | 1.21 |
| 10-23 20:46 | +10 | ETH | UP | 0.64 | 0.74 | 0.69 |
| 10-23 20:46 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 10-23 20:46 | +10 stop | XRP | UP | 0.64 | 0.75 | 0.79 |
| 10-23 20:46 | +20 | XRP | UP | 0.64 | 0.85 | 1.84 |
| 10-23 20:46 | +15 | XRP | UP | 0.68 | 0.85 | 1.45 |
| 10-23 20:46 | +10 | XRP | UP | 0.68 | 0.81 | 1.03 |
| 10-23 20:46 | +5 | XRP | UP | 0.67 | 0.75 | 0.50 |
| 10-23 20:46 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 10-23 20:46 | +20 | SOL | UP | 0.66 | 0.86 | 1.75 |
| 10-23 20:46 | +15 | SOL | UP | 0.66 | 0.82 | 1.33 |
| 10-23 20:46 | +10 | SOL | UP | 0.66 | 0.76 | 0.71 |
