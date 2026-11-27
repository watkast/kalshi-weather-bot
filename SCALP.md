# Range-Scalp Bot

*Updated Fri Nov 27 04:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73250 | 63927 | 9323 (164) | 4 | $-19524.26 | -4.2% |
| **+10¢** | 54600 | 43714 | 10886 (210) | 5 | $-18131.84 | -5.3% |
| **+15¢** | 45725 | 33998 | 11727 (268) | 5 | $-16235.43 | -5.7% |
| **+20¢** | 40694 | 28344 | 12350 (334) | 5 | $-14643.52 | -5.7% |
| **+10¢ (15¢ stop)** | 89227 | 89015 | 212 (129) | 0 | $-32968.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 03:58 | +5 | HYPE | DOWN | 0.44 | 0.60 | 1.25 |
| 11-27 03:58 | +10 stop | HYPE | DOWN | 0.52 | 0.15 | -3.97 |
| 11-27 03:58 | +20 | HYPE | DOWN | 0.52 | open |  |
| 11-27 03:58 | +15 | HYPE | DOWN | 0.52 | open |  |
| 11-27 03:58 | +10 | HYPE | DOWN | 0.52 | open |  |
| 11-27 03:58 | +5 | HYPE | DOWN | 0.52 | 0.60 | 0.45 |
| 11-27 03:57 | +10 stop | ETH | DOWN | 0.57 | 0.71 | 1.07 |
| 11-27 03:57 | +10 stop | ZEC | UP | 0.58 | 0.72 | 1.07 |
| 11-27 03:55 | +10 stop | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-27 03:55 | +10 stop | ETH | UP | 0.59 | 0.33 | -2.93 |
| 11-27 03:55 | +15 | ETH | UP | 0.59 | open |  |
| 11-27 03:55 | +10 | ETH | UP | 0.59 | open |  |
| 11-27 03:55 | +5 | ETH | UP | 0.58 | open |  |
| 11-27 03:55 | +10 stop | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-27 03:55 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-27 03:55 | +5 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 11-27 03:55 | +10 stop | BNB | UP | 0.37 | 0.55 | 1.45 |
| 11-27 03:54 | +5 | HYPE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-27 03:53 | +10 stop | XRP | DOWN | 0.67 | 0.84 | 1.44 |
| 11-27 03:53 | +20 | XRP | DOWN | 0.66 | 0.86 | 1.79 |
| 11-27 03:53 | +15 | XRP | DOWN | 0.65 | 0.84 | 1.64 |
| 11-27 03:53 | +10 | XRP | DOWN | 0.67 | 0.84 | 1.49 |
| 11-27 03:53 | +5 | XRP | DOWN | 0.67 | 0.75 | 0.50 |
| 11-27 03:52 | +10 stop | BNB | DOWN | 0.56 | 0.41 | -1.85 |
| 11-27 03:52 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-27 03:52 | +10 stop | ETH | UP | 0.61 | 0.72 | 0.78 |
| 11-27 03:52 | +10 | ETH | UP | 0.61 | 0.72 | 0.78 |
| 11-27 03:52 | +5 | ETH | UP | 0.61 | 0.68 | 0.37 |
| 11-27 03:52 | +10 stop | HYPE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-27 03:51 | +10 stop | BTC | UP | 0.65 | 0.39 | -2.93 |
| 11-27 03:51 | +10 stop | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 11-27 03:51 | +15 | DOGE | DOWN | 0.63 | 0.80 | 1.41 |
| 11-27 03:51 | +10 | DOGE | DOWN | 0.62 | 0.76 | 1.10 |
| 11-27 03:51 | +5 | DOGE | DOWN | 0.62 | 0.76 | 1.10 |
| 11-27 03:51 | +10 stop | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 11-27 03:51 | +20 | NEAR | DOWN | 0.70 | 0.92 | 2.00 |
| 11-27 03:51 | +15 | NEAR | DOWN | 0.70 | 0.87 | 1.47 |
| 11-27 03:51 | +10 | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 11-27 03:51 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 11-27 03:51 | +10 stop | ZEC | DOWN | 0.48 | 0.62 | 1.05 |
