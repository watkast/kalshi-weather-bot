# Range-Scalp Bot

*Updated Mon Nov 16 08:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61743 | 53869 | 7874 (115) | 0 | $-16675.07 | -4.3% |
| **+10¢** | 46126 | 36903 | 9223 (157) | 1 | $-15602.47 | -5.4% |
| **+15¢** | 38652 | 28703 | 9949 (196) | 1 | $-14235.68 | -5.9% |
| **+20¢** | 34458 | 24024 | 10434 (249) | 1 | $-12446.71 | -5.8% |
| **+10¢ (15¢ stop)** | 75148 | 74994 | 154 (90) | 1 | $-27677.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 08:00 | +10 stop | DOGE | DOWN | 0.67 | open |  |
| 11-16 08:00 | +20 | DOGE | DOWN | 0.67 | open |  |
| 11-16 08:00 | +15 | DOGE | DOWN | 0.67 | open |  |
| 11-16 08:00 | +10 | DOGE | DOWN | 0.67 | open |  |
| 11-16 08:00 | +5 | DOGE | DOWN | 0.67 | 0.75 | 0.50 |
| 11-16 07:57 | +5 | BNB | DOWN | 0.45 | 0.56 | 0.74 |
| 11-16 07:56 | +10 stop | BNB | UP | 0.47 | 0.63 | 1.25 |
| 11-16 07:56 | +15 | BNB | UP | 0.47 | 0.63 | 1.25 |
| 11-16 07:56 | +10 | BNB | UP | 0.46 | 0.63 | 1.35 |
| 11-16 07:56 | +5 | BNB | UP | 0.46 | 0.54 | 0.44 |
| 11-16 07:55 | +10 stop | BNB | DOWN | 0.42 | 0.69 | 2.38 |
| 11-16 07:55 | +15 | BNB | DOWN | 0.43 | 0.69 | 2.31 |
| 11-16 07:55 | +10 | BNB | DOWN | 0.43 | 0.69 | 2.31 |
| 11-16 07:55 | +5 | BNB | DOWN | 0.43 | 0.69 | 2.31 |
| 11-16 07:54 | +10 stop | NEAR | UP | 0.60 | 0.88 | 2.55 |
| 11-16 07:54 | +10 stop | HYPE | DOWN | 0.60 | 0.33 | -3.03 |
| 11-16 07:54 | +10 | HYPE | DOWN | 0.60 | yes | -6.17 |
| 11-16 07:54 | +5 | HYPE | DOWN | 0.60 | yes | -6.17 |
| 11-16 07:53 | +10 stop | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 11-16 07:53 | +10 stop | ETH | UP | 0.64 | 0.83 | 1.63 |
| 11-16 07:52 | +10 stop | ETH | DOWN | 0.66 | 0.41 | -2.83 |
| 11-16 07:52 | +10 stop | DOGE | UP | 0.68 | 0.81 | 1.03 |
| 11-16 07:51 | +10 stop | NEAR | DOWN | 0.66 | 0.51 | -1.88 |
| 11-16 07:50 | +10 stop | NEAR | UP | 0.66 | 0.40 | -2.93 |
| 11-16 07:50 | +10 stop | HYPE | DOWN | 0.56 | 0.69 | 0.97 |
| 11-16 07:50 | +10 stop | BNB | DOWN | 0.58 | 0.70 | 0.87 |
| 11-16 07:50 | +10 stop | ZEC | UP | 0.66 | 0.43 | -2.64 |
| 11-16 07:50 | +10 stop | XRP | UP | 0.69 | 0.48 | -2.43 |
| 11-16 07:50 | +10 stop | BTC | UP | 0.62 | 0.73 | 0.79 |
| 11-16 07:50 | +10 | BTC | UP | 0.62 | 0.73 | 0.79 |
| 11-16 07:50 | +5 | BTC | UP | 0.62 | 0.69 | 0.38 |
| 11-16 07:48 | +10 stop | XRP | DOWN | 0.49 | 0.31 | -2.13 |
| 11-16 07:48 | +5 | BTC | UP | 0.65 | 0.71 | 0.29 |
| 11-16 07:48 | +10 stop | HYPE | UP | 0.66 | 0.51 | -1.84 |
| 11-16 07:48 | +10 stop | ETH | UP | 0.51 | 0.34 | -2.04 |
| 11-16 07:48 | +10 stop | DOGE | UP | 0.62 | 0.74 | 0.91 |
| 11-16 07:48 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-16 07:48 | +20 | BTC | UP | 0.64 | 0.85 | 1.84 |
| 11-16 07:48 | +15 | BTC | UP | 0.64 | 0.80 | 1.31 |
| 11-16 07:48 | +10 | BTC | UP | 0.64 | 0.74 | 0.69 |
