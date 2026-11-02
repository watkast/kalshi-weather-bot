# Range-Scalp Bot

*Updated Mon Nov 02 13:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44909 | 39105 | 5804 (66) | 1 | $-12990.97 | -4.6% |
| **+10¢** | 33525 | 26800 | 6725 (87) | 1 | $-11856.25 | -5.6% |
| **+15¢** | 28041 | 20804 | 7237 (114) | 1 | $-10909.76 | -6.2% |
| **+20¢** | 24913 | 17337 | 7576 (149) | 1 | $-9635.94 | -6.2% |
| **+10¢ (15¢ stop)** | 54810 | 54723 | 87 (51) | 1 | $-20716.03 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 13:21 | +10 stop | HYPE | UP | 0.68 | open |  |
| 11-02 13:20 | +10 stop | HYPE | DOWN | 0.53 | 0.34 | -2.24 |
| 11-02 13:18 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.97 |
| 11-02 13:18 | +10 | BNB | DOWN | 0.67 | 0.79 | 0.97 |
| 11-02 13:18 | +5 | BNB | DOWN | 0.67 | 0.75 | 0.55 |
| 11-02 13:16 | +10 stop | BNB | DOWN | 0.64 | 0.77 | 1.05 |
| 11-02 13:16 | +20 | BNB | DOWN | 0.64 | 0.88 | 2.20 |
| 11-02 13:16 | +15 | BNB | DOWN | 0.64 | 0.79 | 1.26 |
| 11-02 13:16 | +10 | BNB | DOWN | 0.64 | 0.77 | 1.05 |
| 11-02 13:16 | +5 | BNB | DOWN | 0.64 | 0.77 | 1.05 |
| 11-02 13:16 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-02 13:16 | +20 | BTC | DOWN | 0.68 | 0.91 | 2.02 |
| 11-02 13:16 | +15 | BTC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-02 13:16 | +10 | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-02 13:16 | +5 | BTC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-02 13:16 | +10 stop | HYPE | DOWN | 0.63 | 0.45 | -2.19 |
| 11-02 13:16 | +20 | HYPE | DOWN | 0.63 | open |  |
| 11-02 13:16 | +15 | HYPE | DOWN | 0.63 | open |  |
| 11-02 13:16 | +10 | HYPE | DOWN | 0.63 | open |  |
| 11-02 13:16 | +5 | HYPE | DOWN | 0.63 | open |  |
| 11-02 13:10 | +10 stop | ZEC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-02 13:09 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 11-02 13:08 | +10 stop | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-02 13:08 | +10 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-02 13:08 | +5 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-02 13:08 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-02 13:08 | +10 | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-02 13:08 | +5 | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-02 13:08 | +10 stop | NEAR | UP | 0.64 | 0.42 | -2.55 |
| 11-02 13:08 | +15 | NEAR | UP | 0.64 | no | -6.57 |
| 11-02 13:08 | +10 | NEAR | UP | 0.64 | no | -6.57 |
| 11-02 13:08 | +5 | NEAR | UP | 0.64 | no | -6.57 |
| 11-02 13:07 | +5 | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 11-02 13:06 | +10 stop | BTC | DOWN | 0.63 | 0.81 | 1.52 |
| 11-02 13:06 | +10 | BTC | DOWN | 0.63 | 0.81 | 1.52 |
| 11-02 13:06 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-02 13:06 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 11-02 13:06 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 11-02 13:06 | +15 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 11-02 13:06 | +10 | ETH | DOWN | 0.64 | 0.74 | 0.69 |
