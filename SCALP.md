# Range-Scalp Bot

*Updated Tue Nov 10 17:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54832 | 47829 | 7003 (91) | 4 | $-14935.58 | -4.3% |
| **+10¢** | 40967 | 32797 | 8170 (121) | 5 | $-13849.43 | -5.4% |
| **+15¢** | 34340 | 25534 | 8806 (155) | 6 | $-12593.39 | -5.8% |
| **+20¢** | 30574 | 21334 | 9240 (204) | 6 | $-11019.93 | -5.7% |
| **+10¢ (15¢ stop)** | 66808 | 66694 | 114 (70) | 0 | $-24720.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 17:52 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 11-10 17:49 | +10 stop | DOGE | UP | 0.69 | 0.85 | 1.36 |
| 11-10 17:49 | +20 | DOGE | UP | 0.69 | 0.89 | 1.78 |
| 11-10 17:49 | +15 | DOGE | UP | 0.69 | 0.85 | 1.36 |
| 11-10 17:49 | +10 | DOGE | UP | 0.69 | 0.85 | 1.36 |
| 11-10 17:49 | +5 | DOGE | UP | 0.69 | 0.74 | 0.21 |
| 11-10 17:49 | +10 stop | NEAR | UP | 0.62 | 0.74 | 0.89 |
| 11-10 17:49 | +10 | BNB | UP | 0.70 | 0.82 | 0.94 |
| 11-10 17:49 | +5 | BNB | UP | 0.70 | 0.82 | 0.90 |
| 11-10 17:49 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-10 17:49 | +10 stop | SOL | DOWN | 0.53 | 0.31 | -2.53 |
| 11-10 17:49 | +10 stop | BNB | UP | 0.70 | 0.82 | 0.94 |
| 11-10 17:49 | +15 | BNB | UP | 0.70 | 0.87 | 1.43 |
| 11-10 17:49 | +10 stop | ETH | UP | 0.71 | 0.82 | 0.84 |
| 11-10 17:49 | +5 | ETH | UP | 0.71 | 0.77 | 0.32 |
| 11-10 17:48 | +10 stop | NEAR | UP | 0.69 | 0.54 | -1.83 |
| 11-10 17:48 | +10 stop | ZEC | UP | 0.57 | 0.30 | -3.03 |
| 11-10 17:48 | +10 stop | SOL | UP | 0.60 | 0.42 | -2.15 |
| 11-10 17:48 | +10 stop | BTC | UP | 0.68 | 0.84 | 1.34 |
| 11-10 17:47 | +10 stop | BNB | UP | 0.58 | 0.75 | 1.38 |
| 11-10 17:47 | +20 | BNB | UP | 0.59 | 0.82 | 2.02 |
| 11-10 17:47 | +15 | BNB | UP | 0.57 | 0.75 | 1.48 |
| 11-10 17:47 | +10 | BNB | UP | 0.59 | 0.75 | 1.29 |
| 11-10 17:47 | +5 | BNB | UP | 0.59 | 0.65 | 0.27 |
| 11-10 17:47 | +10 stop | ETH | UP | 0.67 | 0.77 | 0.71 |
| 11-10 17:47 | +5 | ETH | UP | 0.67 | 0.75 | 0.50 |
| 11-10 17:47 | +10 stop | HYPE | UP | 0.59 | 0.71 | 0.88 |
| 11-10 17:47 | +10 stop | NEAR | DOWN | 0.58 | 0.37 | -2.45 |
| 11-10 17:47 | +20 | NEAR | DOWN | 0.60 | open |  |
| 11-10 17:47 | +15 | NEAR | DOWN | 0.60 | open |  |
| 11-10 17:47 | +10 | NEAR | DOWN | 0.60 | open |  |
| 11-10 17:47 | +5 | NEAR | DOWN | 0.60 | open |  |
| 11-10 17:47 | +10 stop | SOL | DOWN | 0.64 | 0.44 | -2.35 |
| 11-10 17:47 | +20 | SOL | DOWN | 0.64 | open |  |
| 11-10 17:47 | +15 | SOL | DOWN | 0.64 | open |  |
| 11-10 17:47 | +10 | SOL | DOWN | 0.64 | open |  |
| 11-10 17:47 | +5 | SOL | DOWN | 0.64 | open |  |
| 11-10 17:46 | +10 stop | BTC | DOWN | 0.53 | 0.34 | -2.24 |
| 11-10 17:46 | +20 | BTC | DOWN | 0.53 | open |  |
| 11-10 17:46 | +15 | BTC | DOWN | 0.53 | open |  |
