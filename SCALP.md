# Range-Scalp Bot

*Updated Wed Nov 11 12:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55839 | 48694 | 7145 (94) | 1 | $-15268.59 | -4.3% |
| **+10¢** | 41721 | 33390 | 8331 (124) | 3 | $-14195.55 | -5.4% |
| **+15¢** | 34981 | 25993 | 8988 (158) | 5 | $-12967.93 | -5.9% |
| **+20¢** | 31157 | 21729 | 9428 (208) | 5 | $-11337.16 | -5.8% |
| **+10¢ (15¢ stop)** | 68014 | 67893 | 121 (73) | 3 | $-25017.29 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 12:46 | +10 stop | ZEC | UP | 0.65 | open |  |
| 11-11 12:46 | +20 | ZEC | UP | 0.65 | open |  |
| 11-11 12:46 | +15 | ZEC | UP | 0.65 | open |  |
| 11-11 12:46 | +10 | ZEC | UP | 0.65 | open |  |
| 11-11 12:46 | +5 | ZEC | UP | 0.65 | open |  |
| 11-11 12:45 | +10 stop | ETH | UP | 0.70 | open |  |
| 11-11 12:45 | +20 | ETH | UP | 0.70 | open |  |
| 11-11 12:45 | +15 | ETH | UP | 0.70 | open |  |
| 11-11 12:45 | +10 | ETH | UP | 0.70 | open |  |
| 11-11 12:45 | +5 | ETH | UP | 0.70 | 0.76 | 0.32 |
| 11-11 12:45 | +10 stop | BTC | UP | 0.65 | 0.76 | 0.81 |
| 11-11 12:45 | +20 | BTC | UP | 0.65 | open |  |
| 11-11 12:45 | +15 | BTC | UP | 0.65 | open |  |
| 11-11 12:45 | +10 | BTC | UP | 0.65 | 0.76 | 0.81 |
| 11-11 12:45 | +5 | BTC | UP | 0.66 | 0.71 | 0.19 |
| 11-11 12:45 | +10 stop | NEAR | UP | 0.58 | open |  |
| 11-11 12:45 | +20 | NEAR | UP | 0.58 | open |  |
| 11-11 12:45 | +15 | NEAR | UP | 0.58 | open |  |
| 11-11 12:45 | +10 | NEAR | UP | 0.58 | open |  |
| 11-11 12:45 | +5 | NEAR | UP | 0.58 | 0.64 | 0.25 |
| 11-11 12:45 | +10 stop | BNB | UP | 0.63 | 0.73 | 0.70 |
| 11-11 12:45 | +20 | BNB | UP | 0.63 | open |  |
| 11-11 12:45 | +15 | BNB | UP | 0.63 | open |  |
| 11-11 12:45 | +10 | BNB | UP | 0.63 | 0.73 | 0.70 |
| 11-11 12:45 | +5 | BNB | UP | 0.63 | 0.73 | 0.70 |
| 11-11 12:39 | +5 | NEAR | DOWN | 0.49 | 0.56 | 0.34 |
| 11-11 12:39 | +10 stop | ZEC | UP | 0.64 | 0.88 | 2.15 |
| 11-11 12:38 | +10 stop | NEAR | DOWN | 0.66 | 0.28 | -4.11 |
| 11-11 12:38 | +20 | NEAR | DOWN | 0.66 | yes | -6.76 |
| 11-11 12:38 | +15 | NEAR | DOWN | 0.66 | yes | -6.76 |
| 11-11 12:38 | +10 | NEAR | DOWN | 0.66 | yes | -6.76 |
| 11-11 12:38 | +5 | NEAR | DOWN | 0.64 | 0.71 | 0.38 |
| 11-11 12:37 | +10 stop | ZEC | DOWN | 0.62 | 0.33 | -3.23 |
| 11-11 12:37 | +20 | ZEC | DOWN | 0.62 | yes | -6.37 |
| 11-11 12:37 | +15 | ZEC | DOWN | 0.62 | yes | -6.37 |
| 11-11 12:37 | +10 | ZEC | DOWN | 0.63 | yes | -6.45 |
| 11-11 12:37 | +5 | ZEC | DOWN | 0.63 | yes | -6.45 |
| 11-11 12:36 | +10 stop | XRP | UP | 0.61 | 0.72 | 0.78 |
| 11-11 12:36 | +10 stop | BNB | UP | 0.71 | 0.88 | 1.47 |
| 11-11 12:35 | +5 | HYPE | DOWN | 0.68 | yes | -6.96 |
