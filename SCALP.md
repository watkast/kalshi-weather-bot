# Range-Scalp Bot

*Updated Sun Nov 08 10:28 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52322 | 45616 | 6706 (82) | 3 | $-14518.96 | -4.4% |
| **+10¢** | 39055 | 31239 | 7816 (107) | 4 | $-13518.88 | -5.5% |
| **+15¢** | 32715 | 24292 | 8423 (137) | 5 | $-12380.29 | -6.0% |
| **+20¢** | 29099 | 20271 | 8828 (181) | 5 | $-10896.89 | -6.0% |
| **+10¢ (15¢ stop)** | 63701 | 63596 | 105 (62) | 0 | $-23548.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 10:26 | +10 stop | BTC | UP | 0.45 | 0.55 | 0.64 |
| 11-08 10:25 | +5 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-08 10:23 | +10 stop | BNB | DOWN | 0.51 | 0.63 | 0.85 |
| 11-08 10:23 | +10 stop | DOGE | DOWN | 0.69 | 0.53 | -1.93 |
| 11-08 10:22 | +10 stop | BTC | DOWN | 0.63 | 0.40 | -2.64 |
| 11-08 10:22 | +10 | BTC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-08 10:22 | +5 | BTC | DOWN | 0.63 | 0.70 | 0.38 |
| 11-08 10:22 | +10 stop | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-08 10:22 | +20 | HYPE | DOWN | 0.67 | 0.90 | 2.10 |
| 11-08 10:22 | +15 | HYPE | DOWN | 0.67 | 0.84 | 1.44 |
| 11-08 10:22 | +10 | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-08 10:22 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.30 |
| 11-08 10:22 | +10 stop | BTC | UP | 0.36 | 0.60 | 2.06 |
| 11-08 10:22 | +10 | BTC | UP | 0.36 | 0.60 | 2.06 |
| 11-08 10:22 | +5 | BTC | UP | 0.36 | 0.60 | 2.06 |
| 11-08 10:22 | +10 stop | BNB | UP | 0.49 | 0.34 | -1.84 |
| 11-08 10:22 | +10 stop | ZEC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-08 10:21 | +10 stop | DOGE | DOWN | 0.70 | 0.54 | -1.93 |
| 11-08 10:20 | +5 | NEAR | DOWN | 0.58 | 0.80 | 1.90 |
| 11-08 10:20 | +10 stop | SOL | UP | 0.71 | 0.34 | -4.01 |
| 11-08 10:20 | +15 | SOL | UP | 0.71 | open |  |
| 11-08 10:20 | +10 | SOL | UP | 0.71 | open |  |
| 11-08 10:20 | +5 | SOL | UP | 0.71 | open |  |
| 11-08 10:20 | +5 | BNB | UP | 0.63 | open |  |
| 11-08 10:20 | +10 stop | ZEC | DOWN | 0.48 | 0.62 | 1.05 |
| 11-08 10:20 | +10 stop | DOGE | UP | 0.70 | 0.39 | -3.42 |
| 11-08 10:20 | +20 | DOGE | UP | 0.70 | open |  |
| 11-08 10:20 | +15 | DOGE | UP | 0.70 | open |  |
| 11-08 10:20 | +10 | DOGE | UP | 0.70 | open |  |
| 11-08 10:20 | +5 | DOGE | UP | 0.70 | open |  |
| 11-08 10:19 | +10 stop | NEAR | UP | 0.50 | 0.17 | -3.58 |
| 11-08 10:19 | +20 | NEAR | UP | 0.50 | open |  |
| 11-08 10:19 | +15 | NEAR | UP | 0.51 | open |  |
| 11-08 10:19 | +10 | NEAR | UP | 0.51 | open |  |
| 11-08 10:19 | +5 | NEAR | UP | 0.51 | 0.58 | 0.34 |
| 11-08 10:18 | +5 | SOL | UP | 0.57 | 0.67 | 0.66 |
| 11-08 10:18 | +5 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-08 10:17 | +5 | SOL | UP | 0.55 | 0.66 | 0.76 |
| 11-08 10:17 | +10 stop | HYPE | UP | 0.63 | 0.73 | 0.69 |
| 11-08 10:17 | +10 | HYPE | UP | 0.63 | 0.73 | 0.69 |
