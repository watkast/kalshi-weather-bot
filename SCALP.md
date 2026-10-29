# Range-Scalp Bot

*Updated Thu Oct 29 00:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38690 | 33759 | 4931 (49) | 4 | $-10890.24 | -4.5% |
| **+10¢** | 28851 | 23158 | 5693 (71) | 7 | $-9657.00 | -5.3% |
| **+15¢** | 24131 | 18014 | 6117 (97) | 7 | $-8623.26 | -5.7% |
| **+20¢** | 21410 | 15005 | 6405 (125) | 8 | $-7519.95 | -5.6% |
| **+10¢ (15¢ stop)** | 47320 | 47253 | 67 (35) | 3 | $-17985.35 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 00:04 | +5 | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 10-29 00:04 | +10 stop | ETH | DOWN | 0.63 | open |  |
| 10-29 00:04 | +10 stop | DOGE | UP | 0.54 | 0.39 | -1.85 |
| 10-29 00:04 | +10 | DOGE | UP | 0.54 | open |  |
| 10-29 00:04 | +10 stop | BTC | DOWN | 0.60 | open |  |
| 10-29 00:04 | +10 stop | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 10-29 00:03 | +10 stop | ZEC | UP | 0.61 | 0.72 | 0.78 |
| 10-29 00:02 | +10 stop | ETH | DOWN | 0.62 | 0.34 | -3.13 |
| 10-29 00:02 | +10 stop | BTC | DOWN | 0.67 | 0.50 | -2.04 |
| 10-29 00:02 | +10 stop | SOL | DOWN | 0.70 | 0.44 | -2.93 |
| 10-29 00:02 | +10 stop | XRP | UP | 0.58 | 0.43 | -1.86 |
| 10-29 00:02 | +20 | XRP | UP | 0.58 | open |  |
| 10-29 00:02 | +15 | XRP | UP | 0.58 | open |  |
| 10-29 00:02 | +10 | XRP | UP | 0.58 | open |  |
| 10-29 00:02 | +5 | XRP | UP | 0.58 | 0.67 | 0.56 |
| 10-29 00:01 | +10 stop | BNB | UP | 0.66 | 0.81 | 1.23 |
| 10-29 00:01 | +20 | BNB | UP | 0.66 | open |  |
| 10-29 00:01 | +15 | BNB | UP | 0.66 | 0.81 | 1.23 |
| 10-29 00:01 | +10 | BNB | UP | 0.66 | 0.81 | 1.23 |
| 10-29 00:01 | +5 | BNB | UP | 0.66 | 0.81 | 1.23 |
| 10-29 00:01 | +10 stop | HYPE | UP | 0.65 | open |  |
| 10-29 00:01 | +20 | HYPE | UP | 0.65 | open |  |
| 10-29 00:01 | +15 | HYPE | UP | 0.65 | open |  |
| 10-29 00:01 | +10 | HYPE | UP | 0.65 | open |  |
| 10-29 00:01 | +5 | HYPE | UP | 0.64 | 0.71 | 0.34 |
| 10-29 00:01 | +10 stop | ZEC | UP | 0.67 | 0.52 | -1.84 |
| 10-29 00:01 | +20 | ZEC | UP | 0.64 | open |  |
| 10-29 00:01 | +15 | ZEC | UP | 0.64 | open |  |
| 10-29 00:01 | +10 | ZEC | UP | 0.64 | open |  |
| 10-29 00:01 | +5 | ZEC | UP | 0.64 | 0.70 | 0.28 |
| 10-29 00:01 | +5 | DOGE | UP | 0.67 | open |  |
| 10-29 00:01 | +10 stop | SOL | UP | 0.62 | 0.38 | -2.74 |
| 10-29 00:01 | +20 | SOL | UP | 0.62 | open |  |
| 10-29 00:01 | +15 | SOL | UP | 0.62 | open |  |
| 10-29 00:01 | +10 | SOL | UP | 0.61 | open |  |
| 10-29 00:01 | +5 | SOL | UP | 0.60 | open |  |
| 10-29 00:01 | +10 stop | ETH | UP | 0.64 | 0.44 | -2.35 |
| 10-29 00:01 | +20 | ETH | UP | 0.64 | open |  |
| 10-29 00:01 | +15 | ETH | UP | 0.64 | open |  |
| 10-29 00:01 | +10 | ETH | UP | 0.64 | open |  |
