# Range-Scalp Bot

*Updated Mon Nov 23 11:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69839 | 60939 | 8900 (146) | 1 | $-18813.04 | -4.3% |
| **+10¢** | 52114 | 41715 | 10399 (189) | 3 | $-17510.74 | -5.3% |
| **+15¢** | 43672 | 32470 | 11202 (245) | 4 | $-15638.40 | -5.7% |
| **+20¢** | 38889 | 27103 | 11786 (310) | 4 | $-13989.69 | -5.7% |
| **+10¢ (15¢ stop)** | 85058 | 84868 | 190 (118) | 3 | $-31248.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 11:01 | +10 stop | BNB | DOWN | 0.52 | open |  |
| 11-23 11:01 | +20 | BNB | DOWN | 0.51 | open |  |
| 11-23 11:01 | +15 | BNB | DOWN | 0.51 | open |  |
| 11-23 11:01 | +10 | BNB | DOWN | 0.50 | open |  |
| 11-23 11:01 | +5 | BNB | DOWN | 0.50 | 0.56 | 0.24 |
| 11-23 11:01 | +10 stop | SOL | DOWN | 0.52 | open |  |
| 11-23 11:01 | +20 | SOL | DOWN | 0.52 | open |  |
| 11-23 11:01 | +15 | SOL | DOWN | 0.52 | open |  |
| 11-23 11:01 | +10 | SOL | DOWN | 0.52 | open |  |
| 11-23 11:01 | +5 | SOL | DOWN | 0.52 | 0.58 | 0.24 |
| 11-23 11:01 | +10 stop | ETH | UP | 0.57 | open |  |
| 11-23 11:01 | +20 | ETH | UP | 0.57 | open |  |
| 11-23 11:01 | +15 | ETH | UP | 0.57 | open |  |
| 11-23 11:01 | +10 | ETH | UP | 0.57 | open |  |
| 11-23 11:01 | +5 | ETH | UP | 0.57 | open |  |
| 11-23 11:01 | +10 stop | ZEC | DOWN | 0.48 | 0.58 | 0.64 |
| 11-23 11:01 | +20 | ZEC | DOWN | 0.48 | open |  |
| 11-23 11:01 | +15 | ZEC | DOWN | 0.48 | open |  |
| 11-23 11:01 | +10 | ZEC | DOWN | 0.48 | 0.58 | 0.64 |
| 11-23 11:01 | +5 | ZEC | DOWN | 0.48 | 0.58 | 0.64 |
| 11-23 10:56 | +10 stop | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-23 10:54 | +10 stop | NEAR | UP | 0.71 | 0.40 | -3.42 |
| 11-23 10:54 | +10 | NEAR | UP | 0.71 | no | -7.25 |
| 11-23 10:54 | +5 | NEAR | UP | 0.70 | no | -7.15 |
| 11-23 10:46 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-23 10:46 | +20 | SOL | UP | 0.71 | 0.93 | 1.99 |
| 11-23 10:46 | +15 | SOL | UP | 0.71 | 0.86 | 1.26 |
| 11-23 10:46 | +10 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-23 10:46 | +5 | SOL | UP | 0.71 | 0.77 | 0.32 |
| 11-23 10:46 | +10 stop | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 11-23 10:46 | +20 | NEAR | UP | 0.69 | no | -7.05 |
| 11-23 10:46 | +15 | NEAR | UP | 0.70 | no | -7.15 |
| 11-23 10:46 | +10 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-23 10:46 | +5 | NEAR | UP | 0.70 | 0.75 | 0.21 |
| 11-23 10:41 | +10 stop | BTC | UP | 0.67 | 0.47 | -2.34 |
| 11-23 10:41 | +20 | BTC | UP | 0.67 | no | -6.86 |
| 11-23 10:41 | +15 | BTC | UP | 0.67 | no | -6.86 |
| 11-23 10:41 | +10 | BTC | UP | 0.67 | no | -6.86 |
| 11-23 10:41 | +5 | BTC | UP | 0.67 | 0.72 | 0.19 |
| 11-23 10:41 | +10 stop | ETH | DOWN | 0.67 | 0.49 | -2.14 |
