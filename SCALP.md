# Range-Scalp Bot

*Updated Wed Nov 11 01:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55166 | 48122 | 7044 (94) | 7 | $-14983.02 | -4.3% |
| **+10¢** | 41216 | 32999 | 8217 (124) | 8 | $-13895.76 | -5.4% |
| **+15¢** | 34554 | 25697 | 8857 (158) | 8 | $-12631.35 | -5.8% |
| **+20¢** | 30764 | 21471 | 9293 (207) | 8 | $-11037.77 | -5.7% |
| **+10¢ (15¢ stop)** | 67201 | 67083 | 118 (73) | 5 | $-24776.92 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 01:07 | +5 | DOGE | DOWN | 0.62 | open |  |
| 11-11 01:07 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 11-11 01:06 | +10 stop | SOL | DOWN | 0.71 | open |  |
| 11-11 01:06 | +10 stop | XRP | DOWN | 0.64 | open |  |
| 11-11 01:06 | +10 stop | DOGE | DOWN | 0.66 | open |  |
| 11-11 01:06 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-11 01:06 | +10 stop | BNB | DOWN | 0.64 | open |  |
| 11-11 01:02 | +10 stop | NEAR | DOWN | 0.67 | 0.83 | 1.33 |
| 11-11 01:02 | +10 | NEAR | DOWN | 0.67 | 0.83 | 1.33 |
| 11-11 01:02 | +10 stop | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 11-11 01:02 | +5 | NEAR | DOWN | 0.68 | 0.76 | 0.51 |
| 11-11 01:02 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-11 01:02 | +10 stop | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-11 01:02 | +5 | DOGE | DOWN | 0.69 | 0.78 | 0.62 |
| 11-11 01:02 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-11 01:01 | +5 | DOGE | UP | 0.54 | 0.68 | 1.06 |
| 11-11 01:01 | +5 | HYPE | UP | 0.46 | 0.53 | 0.34 |
| 11-11 01:01 | +10 stop | NEAR | DOWN | 0.46 | 0.58 | 0.84 |
| 11-11 01:01 | +20 | NEAR | DOWN | 0.46 | 0.67 | 1.76 |
| 11-11 01:01 | +15 | NEAR | DOWN | 0.46 | 0.67 | 1.76 |
| 11-11 01:01 | +10 | NEAR | DOWN | 0.46 | 0.58 | 0.84 |
| 11-11 01:01 | +5 | NEAR | DOWN | 0.46 | 0.54 | 0.44 |
| 11-11 01:01 | +10 stop | ETH | UP | 0.65 | 0.45 | -2.34 |
| 11-11 01:01 | +20 | ETH | UP | 0.66 | open |  |
| 11-11 01:01 | +15 | ETH | UP | 0.66 | open |  |
| 11-11 01:01 | +10 | ETH | UP | 0.65 | open |  |
| 11-11 01:01 | +5 | ETH | UP | 0.65 | open |  |
| 11-11 01:01 | +10 stop | BNB | UP | 0.65 | 0.50 | -1.84 |
| 11-11 01:01 | +20 | BNB | UP | 0.65 | open |  |
| 11-11 01:01 | +15 | BNB | UP | 0.65 | open |  |
| 11-11 01:01 | +10 | BNB | UP | 0.65 | open |  |
| 11-11 01:01 | +5 | BNB | UP | 0.65 | open |  |
| 11-11 01:01 | +10 stop | BTC | UP | 0.64 | 0.47 | -2.05 |
| 11-11 01:01 | +20 | BTC | UP | 0.64 | open |  |
| 11-11 01:01 | +15 | BTC | UP | 0.64 | open |  |
| 11-11 01:01 | +10 | BTC | UP | 0.63 | open |  |
| 11-11 01:01 | +5 | BTC | UP | 0.63 | open |  |
| 11-11 01:01 | +10 stop | XRP | UP | 0.61 | 0.34 | -3.03 |
| 11-11 01:01 | +20 | XRP | UP | 0.61 | open |  |
| 11-11 01:01 | +15 | XRP | UP | 0.61 | open |  |
