# Range-Scalp Bot

*Updated Wed Nov 25 19:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71953 | 62806 | 9147 (158) | 9 | $-19141.84 | -4.2% |
| **+10¢** | 53682 | 42999 | 10683 (203) | 9 | $-17732.20 | -5.3% |
| **+15¢** | 44953 | 33445 | 11508 (260) | 9 | $-15824.82 | -5.6% |
| **+20¢** | 40024 | 27903 | 12121 (326) | 9 | $-14225.73 | -5.7% |
| **+10¢ (15¢ stop)** | 87607 | 87398 | 209 (128) | 0 | $-32141.82 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 19:04 | +10 stop | NEAR | UP | 0.69 | 0.79 | 0.73 |
| 11-25 19:03 | +10 stop | NEAR | UP | 0.57 | 0.69 | 0.87 |
| 11-25 19:03 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 11-25 19:03 | +10 stop | BNB | UP | 0.70 | 0.85 | 1.26 |
| 11-25 19:03 | +10 stop | SOL | UP | 0.63 | 0.73 | 0.69 |
| 11-25 19:03 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-25 19:03 | +10 stop | ETH | UP | 0.67 | 0.81 | 1.13 |
| 11-25 19:02 | +10 stop | ZEC | UP | 0.58 | 0.68 | 0.66 |
| 11-25 19:01 | +5 | DOGE | DOWN | 0.55 | open |  |
| 11-25 19:01 | +10 stop | HYPE | DOWN | 0.51 | 0.29 | -2.53 |
| 11-25 19:01 | +20 | HYPE | DOWN | 0.51 | open |  |
| 11-25 19:01 | +15 | HYPE | DOWN | 0.51 | open |  |
| 11-25 19:01 | +10 | HYPE | DOWN | 0.51 | open |  |
| 11-25 19:01 | +5 | HYPE | DOWN | 0.51 | open |  |
| 11-25 19:01 | +10 stop | XRP | DOWN | 0.50 | 0.30 | -2.33 |
| 11-25 19:01 | +20 | XRP | DOWN | 0.50 | open |  |
| 11-25 19:01 | +15 | XRP | DOWN | 0.52 | open |  |
| 11-25 19:01 | +10 | XRP | DOWN | 0.52 | open |  |
| 11-25 19:01 | +5 | XRP | DOWN | 0.53 | open |  |
| 11-25 19:01 | +10 stop | SOL | DOWN | 0.61 | 0.41 | -2.34 |
| 11-25 19:01 | +20 | SOL | DOWN | 0.61 | open |  |
| 11-25 19:01 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-25 19:01 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-25 19:01 | +5 | SOL | DOWN | 0.62 | open |  |
| 11-25 19:01 | +10 stop | NEAR | DOWN | 0.60 | 0.40 | -2.34 |
| 11-25 19:01 | +20 | NEAR | DOWN | 0.60 | open |  |
| 11-25 19:01 | +15 | NEAR | DOWN | 0.60 | open |  |
| 11-25 19:01 | +10 | NEAR | DOWN | 0.60 | open |  |
| 11-25 19:01 | +5 | NEAR | DOWN | 0.60 | open |  |
| 11-25 19:01 | +10 stop | ETH | DOWN | 0.55 | 0.38 | -2.05 |
| 11-25 19:01 | +20 | ETH | DOWN | 0.55 | open |  |
| 11-25 19:01 | +15 | ETH | DOWN | 0.55 | open |  |
| 11-25 19:01 | +10 | ETH | DOWN | 0.55 | open |  |
| 11-25 19:01 | +5 | ETH | DOWN | 0.55 | open |  |
| 11-25 19:01 | +10 stop | BTC | DOWN | 0.60 | 0.45 | -1.85 |
| 11-25 19:01 | +20 | BTC | DOWN | 0.60 | open |  |
| 11-25 19:01 | +15 | BTC | DOWN | 0.60 | open |  |
| 11-25 19:01 | +10 | BTC | DOWN | 0.59 | open |  |
| 11-25 19:01 | +5 | BTC | DOWN | 0.59 | open |  |
| 11-25 19:01 | +10 stop | BNB | DOWN | 0.52 | 0.33 | -2.24 |
