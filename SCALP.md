# Range-Scalp Bot

*Updated Fri Nov 27 23:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74056 | 64641 | 9415 (171) | 5 | $-19639.89 | -4.2% |
| **+10¢** | 55169 | 44173 | 10996 (216) | 9 | $-18258.83 | -5.3% |
| **+15¢** | 46195 | 34351 | 11844 (274) | 9 | $-16328.95 | -5.6% |
| **+20¢** | 41113 | 28638 | 12475 (341) | 9 | $-14734.32 | -5.7% |
| **+10¢ (15¢ stop)** | 90149 | 89930 | 219 (135) | 6 | $-33329.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 23:50 | +10 stop | BNB | UP | 0.70 | open |  |
| 11-27 23:50 | +10 stop | XRP | DOWN | 0.64 | open |  |
| 11-27 23:50 | +10 stop | BTC | UP | 0.71 | open |  |
| 11-27 23:50 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 11-27 23:49 | +10 stop | DOGE | UP | 0.64 | 0.75 | 0.79 |
| 11-27 23:49 | +10 stop | NEAR | UP | 0.70 | open |  |
| 11-27 23:49 | +5 | NEAR | UP | 0.70 | 0.77 | 0.43 |
| 11-27 23:49 | +10 stop | XRP | DOWN | 0.51 | 0.64 | 0.95 |
| 11-27 23:48 | +10 stop | ZEC | UP | 0.61 | 0.81 | 1.72 |
| 11-27 23:48 | +5 | ZEC | UP | 0.61 | 0.81 | 1.72 |
| 11-27 23:48 | +5 | BTC | UP | 0.57 | 0.62 | 0.15 |
| 11-27 23:48 | +5 | SOL | DOWN | 0.57 | open |  |
| 11-27 23:48 | +10 stop | HYPE | UP | 0.61 | 0.72 | 0.78 |
| 11-27 23:47 | +10 stop | NEAR | UP | 0.49 | 0.60 | 0.76 |
| 11-27 23:47 | +5 | NEAR | UP | 0.49 | 0.60 | 0.75 |
| 11-27 23:47 | +5 | ZEC | UP | 0.53 | 0.60 | 0.35 |
| 11-27 23:47 | +5 | HYPE | UP | 0.60 | 0.69 | 0.58 |
| 11-27 23:47 | +10 stop | ETH | DOWN | 0.57 | open |  |
| 11-27 23:47 | +10 | ETH | DOWN | 0.57 | open |  |
| 11-27 23:47 | +10 stop | BNB | DOWN | 0.58 | 0.36 | -2.55 |
| 11-27 23:47 | +20 | BNB | DOWN | 0.58 | open |  |
| 11-27 23:47 | +15 | BNB | DOWN | 0.58 | open |  |
| 11-27 23:47 | +10 | BNB | DOWN | 0.58 | open |  |
| 11-27 23:47 | +5 | BNB | DOWN | 0.58 | open |  |
| 11-27 23:47 | +10 stop | SOL | DOWN | 0.52 | open |  |
| 11-27 23:47 | +20 | SOL | DOWN | 0.52 | open |  |
| 11-27 23:47 | +15 | SOL | DOWN | 0.52 | open |  |
| 11-27 23:47 | +10 | SOL | DOWN | 0.52 | open |  |
| 11-27 23:47 | +5 | SOL | DOWN | 0.52 | 0.58 | 0.24 |
| 11-27 23:47 | +10 stop | XRP | UP | 0.68 | 0.42 | -2.94 |
| 11-27 23:47 | +20 | XRP | UP | 0.68 | open |  |
| 11-27 23:47 | +15 | XRP | UP | 0.68 | open |  |
| 11-27 23:47 | +10 | XRP | UP | 0.69 | open |  |
| 11-27 23:47 | +5 | XRP | UP | 0.68 | open |  |
| 11-27 23:47 | +5 | DOGE | DOWN | 0.60 | open |  |
| 11-27 23:46 | +10 stop | NEAR | DOWN | 0.61 | 0.39 | -2.50 |
| 11-27 23:46 | +20 | NEAR | DOWN | 0.61 | open |  |
| 11-27 23:46 | +15 | NEAR | DOWN | 0.61 | open |  |
| 11-27 23:46 | +10 | NEAR | DOWN | 0.61 | open |  |
| 11-27 23:46 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.31 |
