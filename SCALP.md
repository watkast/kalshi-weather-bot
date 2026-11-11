# Range-Scalp Bot

*Updated Wed Nov 11 05:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55488 | 48393 | 7095 (94) | 4 | $-15148.53 | -4.3% |
| **+10¢** | 41453 | 33175 | 8278 (124) | 6 | $-14093.15 | -5.4% |
| **+15¢** | 34758 | 25832 | 8926 (158) | 6 | $-12853.43 | -5.9% |
| **+20¢** | 30952 | 21591 | 9361 (207) | 7 | $-11221.43 | -5.8% |
| **+10¢ (15¢ stop)** | 67579 | 67461 | 118 (73) | 0 | $-24876.12 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 05:52 | +10 stop | BTC | UP | 0.71 | 0.87 | 1.37 |
| 11-11 05:52 | +20 | BTC | UP | 0.71 | 0.94 | 2.07 |
| 11-11 05:52 | +15 | BTC | UP | 0.71 | 0.87 | 1.37 |
| 11-11 05:52 | +10 | BTC | UP | 0.71 | 0.87 | 1.37 |
| 11-11 05:52 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 11-11 05:52 | +10 stop | ETH | UP | 0.69 | 0.83 | 1.15 |
| 11-11 05:51 | +10 stop | ZEC | UP | 0.58 | 0.71 | 0.97 |
| 11-11 05:50 | +10 stop | BNB | UP | 0.66 | 0.49 | -2.04 |
| 11-11 05:50 | +10 stop | HYPE | UP | 0.53 | 0.36 | -2.05 |
| 11-11 05:48 | +10 stop | NEAR | UP | 0.68 | 0.80 | 0.92 |
| 11-11 05:48 | +5 | NEAR | UP | 0.69 | 0.80 | 0.83 |
| 11-11 05:48 | +10 stop | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-11 05:48 | +20 | BTC | UP | 0.65 | 0.88 | 2.06 |
| 11-11 05:48 | +15 | BTC | UP | 0.65 | 0.88 | 2.06 |
| 11-11 05:48 | +10 | BTC | UP | 0.65 | 0.77 | 0.91 |
| 11-11 05:48 | +5 | BTC | UP | 0.65 | 0.74 | 0.60 |
| 11-11 05:48 | +10 stop | ZEC | UP | 0.65 | 0.84 | 1.64 |
| 11-11 05:48 | +10 stop | BNB | UP | 0.61 | 0.72 | 0.78 |
| 11-11 05:48 | +10 stop | ETH | UP | 0.56 | 0.70 | 1.07 |
| 11-11 05:48 | +10 stop | HYPE | DOWN | 0.56 | 0.38 | -2.15 |
| 11-11 05:48 | +10 stop | ZEC | DOWN | 0.37 | 0.53 | 1.25 |
| 11-11 05:47 | +10 stop | DOGE | UP | 0.55 | 0.71 | 1.27 |
| 11-11 05:47 | +5 | DOGE | UP | 0.56 | 0.71 | 1.17 |
| 11-11 05:47 | +10 stop | XRP | UP | 0.62 | 0.81 | 1.62 |
| 11-11 05:47 | +10 stop | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-11 05:47 | +20 | SOL | UP | 0.67 | 0.91 | 2.12 |
| 11-11 05:47 | +15 | SOL | UP | 0.67 | 0.86 | 1.65 |
| 11-11 05:47 | +10 | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-11 05:47 | +5 | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-11 05:47 | +10 stop | NEAR | DOWN | 0.56 | 0.35 | -2.44 |
| 11-11 05:47 | +20 | NEAR | DOWN | 0.56 | open |  |
| 11-11 05:47 | +15 | NEAR | DOWN | 0.56 | open |  |
| 11-11 05:47 | +10 | NEAR | DOWN | 0.56 | open |  |
| 11-11 05:47 | +5 | NEAR | DOWN | 0.56 | 0.61 | 0.15 |
| 11-11 05:46 | +10 stop | HYPE | DOWN | 0.66 | 0.48 | -2.14 |
| 11-11 05:46 | +20 | HYPE | DOWN | 0.66 | open |  |
| 11-11 05:46 | +15 | HYPE | DOWN | 0.66 | 0.83 | 1.44 |
| 11-11 05:46 | +10 | HYPE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-11 05:46 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-11 05:46 | +10 stop | ETH | DOWN | 0.61 | 0.46 | -1.85 |
