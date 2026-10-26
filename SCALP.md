# Range-Scalp Bot

*Updated Mon Oct 26 20:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35379 | 30884 | 4495 (43) | 0 | $-9855.27 | -4.4% |
| **+10¢** | 26461 | 21259 | 5202 (65) | 3 | $-8694.30 | -5.2% |
| **+15¢** | 22142 | 16542 | 5600 (89) | 6 | $-7796.05 | -5.6% |
| **+20¢** | 19635 | 13766 | 5869 (112) | 7 | $-6850.10 | -5.6% |
| **+10¢ (15¢ stop)** | 43377 | 43315 | 62 (33) | 2 | $-16515.58 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 20:32 | +5 | SOL | UP | 0.70 | 0.77 | 0.42 |
| 10-26 20:32 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-26 20:32 | +20 | DOGE | UP | 0.71 | open |  |
| 10-26 20:32 | +15 | DOGE | UP | 0.71 | open |  |
| 10-26 20:32 | +10 | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-26 20:32 | +5 | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 10-26 20:32 | +10 stop | NEAR | UP | 0.70 | open |  |
| 10-26 20:32 | +20 | NEAR | UP | 0.70 | open |  |
| 10-26 20:32 | +15 | NEAR | UP | 0.70 | open |  |
| 10-26 20:32 | +10 | NEAR | UP | 0.70 | open |  |
| 10-26 20:32 | +5 | NEAR | UP | 0.70 | 0.77 | 0.42 |
| 10-26 20:32 | +10 stop | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 10-26 20:32 | +20 | HYPE | UP | 0.57 | open |  |
| 10-26 20:32 | +15 | HYPE | UP | 0.57 | open |  |
| 10-26 20:32 | +10 | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 10-26 20:32 | +5 | HYPE | UP | 0.57 | 0.65 | 0.46 |
| 10-26 20:32 | +10 stop | ETH | UP | 0.65 | 0.75 | 0.70 |
| 10-26 20:32 | +20 | ETH | UP | 0.65 | open |  |
| 10-26 20:32 | +15 | ETH | UP | 0.65 | open |  |
| 10-26 20:32 | +10 | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-26 20:32 | +5 | ETH | UP | 0.66 | 0.75 | 0.60 |
| 10-26 20:32 | +10 stop | BNB | UP | 0.71 | open |  |
| 10-26 20:32 | +20 | BNB | UP | 0.71 | open |  |
| 10-26 20:32 | +15 | BNB | UP | 0.71 | open |  |
| 10-26 20:32 | +10 | BNB | UP | 0.71 | open |  |
| 10-26 20:32 | +5 | BNB | UP | 0.71 | 0.79 | 0.53 |
| 10-26 20:31 | +10 stop | BTC | UP | 0.67 | 0.82 | 1.23 |
| 10-26 20:31 | +20 | BTC | UP | 0.67 | open |  |
| 10-26 20:31 | +15 | BTC | UP | 0.67 | 0.82 | 1.23 |
| 10-26 20:31 | +10 | BTC | UP | 0.67 | 0.82 | 1.23 |
| 10-26 20:31 | +5 | BTC | UP | 0.67 | 0.73 | 0.30 |
| 10-26 20:31 | +10 stop | ZEC | UP | 0.57 | 0.68 | 0.76 |
| 10-26 20:31 | +20 | ZEC | UP | 0.57 | 0.80 | 2.00 |
| 10-26 20:31 | +15 | ZEC | UP | 0.57 | 0.76 | 1.59 |
| 10-26 20:31 | +10 | ZEC | UP | 0.57 | 0.68 | 0.76 |
| 10-26 20:31 | +5 | ZEC | UP | 0.57 | 0.62 | 0.15 |
| 10-26 20:31 | +10 stop | SOL | DOWN | 0.51 | 0.25 | -2.92 |
| 10-26 20:31 | +20 | SOL | DOWN | 0.51 | open |  |
| 10-26 20:31 | +15 | SOL | DOWN | 0.52 | open |  |
| 10-26 20:31 | +10 | SOL | DOWN | 0.52 | open |  |
