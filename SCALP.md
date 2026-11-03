# Range-Scalp Bot

*Updated Tue Nov 03 00:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45377 | 39511 | 5866 (67) | 9 | $-13112.73 | -4.6% |
| **+10¢** | 33869 | 27072 | 6797 (89) | 9 | $-11987.13 | -5.6% |
| **+15¢** | 28329 | 21016 | 7313 (116) | 9 | $-11028.20 | -6.2% |
| **+20¢** | 25158 | 17499 | 7659 (151) | 9 | $-9795.90 | -6.2% |
| **+10¢ (15¢ stop)** | 55377 | 55290 | 87 (51) | 2 | $-20910.58 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 00:56 | +10 stop | ETH | UP | 0.68 | open |  |
| 11-03 00:56 | +10 stop | BTC | DOWN | 0.66 | open |  |
| 11-03 00:56 | +15 | BTC | DOWN | 0.66 | open |  |
| 11-03 00:54 | +10 stop | ETH | DOWN | 0.68 | 0.35 | -3.62 |
| 11-03 00:54 | +10 | ETH | DOWN | 0.68 | open |  |
| 11-03 00:54 | +5 | ETH | DOWN | 0.68 | open |  |
| 11-03 00:54 | +20 | BTC | DOWN | 0.67 | open |  |
| 11-03 00:53 | +15 | BTC | DOWN | 0.62 | 0.80 | 1.51 |
| 11-03 00:53 | +10 stop | BNB | DOWN | 0.65 | 0.80 | 1.22 |
| 11-03 00:53 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-03 00:53 | +10 stop | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-03 00:53 | +10 stop | ETH | UP | 0.49 | 0.62 | 0.95 |
| 11-03 00:53 | +10 | ETH | UP | 0.50 | 0.62 | 0.85 |
| 11-03 00:53 | +5 | ETH | UP | 0.49 | 0.62 | 0.95 |
| 11-03 00:52 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 11-03 00:52 | +10 stop | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 11-03 00:52 | +10 stop | ZEC | DOWN | 0.57 | 0.70 | 0.97 |
| 11-03 00:51 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-03 00:51 | +10 stop | BTC | UP | 0.64 | 0.47 | -2.05 |
| 11-03 00:51 | +10 | BTC | UP | 0.64 | open |  |
| 11-03 00:51 | +5 | BTC | UP | 0.65 | open |  |
| 11-03 00:51 | +10 stop | BNB | UP | 0.57 | 0.41 | -1.95 |
| 11-03 00:50 | +10 stop | DOGE | UP | 0.68 | 0.48 | -2.34 |
| 11-03 00:50 | +10 stop | SOL | DOWN | 0.51 | 0.67 | 1.26 |
| 11-03 00:50 | +10 stop | HYPE | DOWN | 0.55 | 0.68 | 0.92 |
| 11-03 00:48 | +5 | BTC | UP | 0.51 | 0.62 | 0.75 |
| 11-03 00:48 | +10 stop | XRP | UP | 0.69 | 0.49 | -2.33 |
| 11-03 00:48 | +20 | XRP | UP | 0.70 | open |  |
| 11-03 00:48 | +15 | XRP | UP | 0.70 | open |  |
| 11-03 00:48 | +10 | XRP | UP | 0.70 | open |  |
| 11-03 00:48 | +5 | XRP | UP | 0.70 | open |  |
| 11-03 00:48 | +10 stop | BNB | UP | 0.67 | 0.51 | -1.94 |
| 11-03 00:48 | +20 | BNB | UP | 0.67 | open |  |
| 11-03 00:48 | +15 | BNB | UP | 0.67 | open |  |
| 11-03 00:48 | +10 | BNB | UP | 0.67 | open |  |
| 11-03 00:48 | +5 | BNB | UP | 0.67 | open |  |
| 11-03 00:48 | +10 stop | SOL | UP | 0.61 | 0.46 | -1.85 |
| 11-03 00:48 | +20 | SOL | UP | 0.61 | open |  |
| 11-03 00:48 | +15 | SOL | UP | 0.61 | open |  |
| 11-03 00:48 | +10 | SOL | UP | 0.61 | open |  |
