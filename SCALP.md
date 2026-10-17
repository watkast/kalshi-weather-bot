# Range-Scalp Bot

*Updated Sat Oct 17 01:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 20148 | 17520 | 2628 (29) | 6 | $-5995.16 | -4.7% |
| **+10¢** | 15171 | 12135 | 3036 (41) | 7 | $-5388.84 | -5.6% |
| **+15¢** | 12688 | 9421 | 3267 (60) | 7 | $-4889.05 | -6.1% |
| **+20¢** | 11252 | 7830 | 3422 (79) | 7 | $-4341.39 | -6.1% |
| **+10¢ (15¢ stop)** | 24771 | 24721 | 50 (29) | 2 | $-9415.71 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 01:07 | +5 | BNB | UP | 0.67 | open |  |
| 10-17 01:07 | +10 stop | ETH | DOWN | 0.71 | open |  |
| 10-17 01:07 | +10 stop | ZEC | UP | 0.67 | 0.47 | -2.34 |
| 10-17 01:07 | +10 stop | BNB | UP | 0.64 | open |  |
| 10-17 01:07 | +10 stop | NEAR | UP | 0.69 | 0.47 | -2.52 |
| 10-17 01:07 | +5 | NEAR | UP | 0.68 | open |  |
| 10-17 01:06 | +10 stop | HYPE | UP | 0.64 | 0.44 | -2.33 |
| 10-17 01:06 | +10 | HYPE | UP | 0.64 | open |  |
| 10-17 01:06 | +5 | HYPE | UP | 0.64 | open |  |
| 10-17 01:06 | +10 stop | BTC | DOWN | 0.56 | 0.66 | 0.66 |
| 10-17 01:06 | +10 stop | SOL | UP | 0.70 | 0.55 | -1.83 |
| 10-17 01:05 | +10 stop | SOL | DOWN | 0.47 | 0.28 | -2.23 |
| 10-17 01:04 | +10 stop | NEAR | UP | 0.61 | 0.79 | 1.51 |
| 10-17 01:04 | +5 | NEAR | UP | 0.61 | 0.67 | 0.27 |
| 10-17 01:04 | +10 stop | HYPE | UP | 0.64 | 0.76 | 0.88 |
| 10-17 01:04 | +15 | HYPE | UP | 0.64 | open |  |
| 10-17 01:04 | +10 | HYPE | UP | 0.64 | 0.76 | 0.88 |
| 10-17 01:04 | +5 | HYPE | UP | 0.64 | 0.73 | 0.55 |
| 10-17 01:04 | +10 stop | ETH | DOWN | 0.67 | 0.47 | -2.34 |
| 10-17 01:04 | +20 | ETH | DOWN | 0.67 | open |  |
| 10-17 01:04 | +15 | ETH | DOWN | 0.68 | open |  |
| 10-17 01:04 | +10 | ETH | DOWN | 0.68 | open |  |
| 10-17 01:04 | +5 | ETH | DOWN | 0.68 | 0.75 | 0.40 |
| 10-17 01:03 | +10 stop | BNB | DOWN | 0.59 | 0.39 | -2.34 |
| 10-17 01:02 | +10 stop | SOL | UP | 0.65 | 0.49 | -1.94 |
| 10-17 01:02 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-17 01:02 | +20 | XRP | DOWN | 0.64 | 0.85 | 1.84 |
| 10-17 01:02 | +15 | XRP | DOWN | 0.64 | 0.81 | 1.42 |
| 10-17 01:02 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-17 01:02 | +5 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-17 01:02 | +10 stop | BNB | UP | 0.57 | 0.40 | -2.05 |
| 10-17 01:02 | +5 | BNB | UP | 0.63 | 0.68 | 0.17 |
| 10-17 01:01 | +10 stop | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 10-17 01:01 | +20 | HYPE | UP | 0.68 | open |  |
| 10-17 01:01 | +15 | HYPE | UP | 0.68 | 0.84 | 1.34 |
| 10-17 01:01 | +10 | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 10-17 01:01 | +5 | HYPE | UP | 0.68 | 0.76 | 0.51 |
| 10-17 01:01 | +10 stop | NEAR | DOWN | 0.56 | 0.31 | -2.83 |
| 10-17 01:01 | +20 | NEAR | DOWN | 0.56 | open |  |
| 10-17 01:01 | +15 | NEAR | DOWN | 0.56 | open |  |
