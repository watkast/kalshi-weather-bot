# Range-Scalp Bot

*Updated Sun Oct 25 19:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 33601 | 29322 | 4279 (43) | 1 | $-9399.19 | -4.4% |
| **+10¢** | 25143 | 20191 | 4952 (65) | 2 | $-8315.21 | -5.3% |
| **+15¢** | 21031 | 15701 | 5330 (89) | 2 | $-7451.72 | -5.6% |
| **+20¢** | 18636 | 13056 | 5580 (111) | 2 | $-6550.35 | -5.6% |
| **+10¢ (15¢ stop)** | 41165 | 41103 | 62 (33) | 0 | $-15696.20 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 18:58 | +10 stop | BTC | DOWN | 0.71 | 0.17 | -5.65 |
| 10-25 18:57 | +5 | ZEC | DOWN | 0.63 | 0.81 | 1.52 |
| 10-25 18:56 | +10 stop | BTC | UP | 0.59 | 0.36 | -2.60 |
| 10-25 18:54 | +10 stop | HYPE | UP | 0.60 | 0.26 | -3.71 |
| 10-25 18:53 | +10 stop | DOGE | DOWN | 0.60 | 0.77 | 1.40 |
| 10-25 18:53 | +5 | ZEC | DOWN | 0.61 | 0.67 | 0.27 |
| 10-25 18:53 | +10 stop | BTC | DOWN | 0.59 | 0.38 | -2.44 |
| 10-25 18:53 | +10 stop | ZEC | DOWN | 0.61 | 0.81 | 1.72 |
| 10-25 18:53 | +10 stop | ETH | DOWN | 0.63 | 0.78 | 1.20 |
| 10-25 18:52 | +10 stop | DOGE | UP | 0.55 | 0.37 | -2.15 |
| 10-25 18:52 | +10 | DOGE | UP | 0.55 | no | -5.68 |
| 10-25 18:52 | +10 stop | XRP | DOWN | 0.66 | 0.77 | 0.81 |
| 10-25 18:52 | +5 | DOGE | UP | 0.61 | no | -6.27 |
| 10-25 18:51 | +10 stop | BTC | DOWN | 0.70 | 0.53 | -2.03 |
| 10-25 18:51 | +10 stop | DOGE | UP | 0.48 | 0.58 | 0.64 |
| 10-25 18:51 | +20 | DOGE | UP | 0.48 | no | -4.98 |
| 10-25 18:51 | +15 | DOGE | UP | 0.48 | no | -4.98 |
| 10-25 18:51 | +10 | DOGE | UP | 0.48 | 0.58 | 0.64 |
| 10-25 18:51 | +5 | DOGE | UP | 0.48 | 0.54 | 0.24 |
| 10-25 18:51 | +10 stop | XRP | DOWN | 0.58 | 0.72 | 1.07 |
| 10-25 18:51 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 10-25 18:51 | +10 stop | HYPE | UP | 0.67 | 0.51 | -1.94 |
| 10-25 18:51 | +10 stop | ETH | UP | 0.62 | 0.45 | -2.05 |
| 10-25 18:51 | +10 | ETH | UP | 0.63 | no | -6.47 |
| 10-25 18:51 | +5 | ETH | UP | 0.63 | no | -6.47 |
| 10-25 18:49 | +5 | BNB | UP | 0.71 | 0.84 | 1.05 |
| 10-25 18:49 | +10 stop | ZEC | UP | 0.67 | 0.50 | -2.04 |
| 10-25 18:49 | +15 | ZEC | UP | 0.67 | open |  |
| 10-25 18:48 | +5 | BTC | UP | 0.69 | 0.81 | 0.94 |
| 10-25 18:48 | +10 stop | XRP | UP | 0.68 | 0.44 | -2.74 |
| 10-25 18:48 | +20 | XRP | UP | 0.68 | open |  |
| 10-25 18:48 | +15 | XRP | UP | 0.68 | open |  |
| 10-25 18:48 | +10 | XRP | UP | 0.69 | open |  |
| 10-25 18:48 | +5 | XRP | UP | 0.69 | open |  |
| 10-25 18:48 | +10 stop | BTC | UP | 0.64 | 0.42 | -2.55 |
| 10-25 18:48 | +10 | BTC | UP | 0.64 | 0.81 | 1.42 |
| 10-25 18:48 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 10-25 18:48 | +10 stop | ETH | UP | 0.63 | 0.77 | 1.10 |
| 10-25 18:48 | +15 | ETH | UP | 0.63 | no | -6.47 |
| 10-25 18:48 | +10 | ETH | UP | 0.64 | 0.77 | 1.00 |
