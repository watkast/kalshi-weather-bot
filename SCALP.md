# Range-Scalp Bot

*Updated Mon Nov 16 20:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62182 | 54250 | 7932 (117) | 3 | $-16823.55 | -4.3% |
| **+10¢** | 46433 | 37152 | 9281 (159) | 4 | $-15692.61 | -5.4% |
| **+15¢** | 38905 | 28892 | 10013 (200) | 4 | $-14304.67 | -5.9% |
| **+20¢** | 34681 | 24181 | 10500 (255) | 4 | $-12480.33 | -5.7% |
| **+10¢ (15¢ stop)** | 75694 | 75538 | 156 (92) | 2 | $-27955.14 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 20:10 | +10 stop | ETH | UP | 0.55 | open |  |
| 11-16 20:10 | +5 | ZEC | UP | 0.67 | open |  |
| 11-16 20:07 | +10 stop | ZEC | UP | 0.71 | open |  |
| 11-16 20:07 | +10 stop | ETH | UP | 0.60 | 0.72 | 0.88 |
| 11-16 20:07 | +10 stop | XRP | UP | 0.71 | 0.83 | 0.95 |
| 11-16 20:07 | +10 | XRP | UP | 0.70 | 0.83 | 1.05 |
| 11-16 20:07 | +5 | XRP | UP | 0.68 | 0.74 | 0.30 |
| 11-16 20:07 | +10 stop | BNB | UP | 0.59 | 0.70 | 0.78 |
| 11-16 20:07 | +5 | BNB | UP | 0.59 | 0.70 | 0.76 |
| 11-16 20:06 | +10 stop | ZEC | UP | 0.51 | 0.63 | 0.85 |
| 11-16 20:05 | +10 stop | ZEC | DOWN | 0.57 | 0.37 | -2.35 |
| 11-16 20:05 | +10 stop | XRP | UP | 0.58 | 0.69 | 0.77 |
| 11-16 20:05 | +10 | XRP | UP | 0.58 | 0.69 | 0.77 |
| 11-16 20:05 | +5 | XRP | UP | 0.58 | 0.69 | 0.77 |
| 11-16 20:05 | +5 | ETH | DOWN | 0.58 | open |  |
| 11-16 20:04 | +5 | XRP | UP | 0.64 | 0.74 | 0.69 |
| 11-16 20:03 | +5 | ETH | DOWN | 0.48 | 0.57 | 0.54 |
| 11-16 20:02 | +10 stop | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 11-16 20:02 | +20 | DOGE | UP | 0.70 | 0.92 | 1.99 |
| 11-16 20:02 | +15 | DOGE | UP | 0.70 | 0.87 | 1.47 |
| 11-16 20:02 | +10 | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 11-16 20:02 | +5 | DOGE | UP | 0.70 | 0.79 | 0.63 |
| 11-16 20:02 | +10 stop | ZEC | UP | 0.69 | 0.53 | -1.93 |
| 11-16 20:02 | +20 | ZEC | UP | 0.71 | open |  |
| 11-16 20:02 | +15 | ZEC | UP | 0.71 | open |  |
| 11-16 20:02 | +10 | ZEC | UP | 0.71 | open |  |
| 11-16 20:02 | +5 | ZEC | UP | 0.71 | 0.78 | 0.42 |
| 11-16 20:02 | +5 | BNB | UP | 0.67 | 0.72 | 0.19 |
| 11-16 20:01 | +10 stop | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-16 20:01 | +20 | XRP | UP | 0.63 | 0.83 | 1.73 |
| 11-16 20:01 | +15 | XRP | UP | 0.63 | 0.83 | 1.73 |
| 11-16 20:01 | +10 | XRP | UP | 0.63 | 0.74 | 0.79 |
| 11-16 20:01 | +5 | XRP | UP | 0.63 | 0.69 | 0.28 |
| 11-16 20:01 | +10 stop | BTC | DOWN | 0.47 | 0.29 | -2.13 |
| 11-16 20:01 | +20 | BTC | DOWN | 0.50 | open |  |
| 11-16 20:01 | +15 | BTC | DOWN | 0.51 | open |  |
| 11-16 20:01 | +10 | BTC | DOWN | 0.51 | open |  |
| 11-16 20:01 | +5 | BTC | DOWN | 0.53 | open |  |
| 11-16 20:01 | +10 stop | BNB | DOWN | 0.46 | 0.28 | -2.13 |
| 11-16 20:01 | +20 | BNB | DOWN | 0.46 | open |  |
